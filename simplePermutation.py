# Algorythm that encrypts a code with the permutation of the alphabet

# Libraries

import pyperclip as PC
import random
import sys

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'

def main():
    option = int(input("""\nSelect an option
1. Code
2. Decode
3. Generate key
"""))

    if option == 1:
        mode = 'code'
        msg = input('Message > ')
        key = input('Key > ')
        checkKey(key)
        text = codeMsg(msg, key)
    
    elif option == 2:
        mode = 'decode'
        msg = input('Message > ')
        key = input('Key > ')
        text = decodeMsg(msg, key)
        checkKey(key)

    elif option == 3:
        key = randKey()
        print('Key: ', key)
        sys.exit()

    print('\nKey %s' % (key))
    print('The %s message is:' % (mode))
    print('  ', text)
    PC.copy(text)
    print()
    print('The message has been copied to the clipboard')


def checkKey(key):
    keyList = list(key)
    symbList = list(SYMBOLS)
    keyList.sort()
    symbList.sort()
    if keyList != symbList:
        print('Incorrect key')
        sys.exit()

def codeMsg(msg, key):
    return msgCod(msg, key, 'code').upper()

def decodeMsg(msg, key):
    return msgCode(msg, key, 'decode').lower()

def msgCod(msg, key, mode):
    text = ''
    carsA = SYMBOLS
    carsB = key
    if mode == 'decode':
        carsA, carsB = carsB, carsA

    for symbol in msg:
        if symbol.upper() in carsA:
            index = carsA.find(symbol.upper())
            if symbol.isupper():
                text += carsB[index].upper()
            else:
                text += carsB[index].lower()

        else:
            text += symbol
    
    return text

def randKey():
    key = list(SYMBOLS)
    random.shuffle(key)
    PC.copy(''.join(key))
    return ''.join(key)

if __name__ == '__main__':
    main()
