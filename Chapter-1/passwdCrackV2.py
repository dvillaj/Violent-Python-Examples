#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib


def testPass(user, cryptPass):
    dictFile = open('dictionary.txt', 'r')
    words = dictFile.readlines() + list(user)

    for word in words:
        word = word.strip('\n')
        cryptWord = hashlib.sha512(word.encode('utf-8')).hexdigest()
        if cryptWord == cryptPass:
            print('[+] Found Password: ' + word + '\n')
            return
    print('[-] Password Not Found.\n')
    return


def main():
    passFile = open('shadow')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print('[*] Cracking Password For: ' + user)
            testPass(user, cryptPass)


if __name__ == '__main__':
    main()
