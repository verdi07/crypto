# Cypher a message with the Cesar method

import pyperclip

ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

exit = ''

mode = input('Do you want to chyper or decypher the code? (c/D)')

# Text and key
text = input('Enter the text: ')
key = int(input('Enter the key (1-25): '))

for symbol in text.upper():
    if symbol in ALPH:
        pos = ALPH.index(symbol)

        if mode == 'c':
            pos = (pos + key) % 26
        if mode == 'D':
            pos = (pos - key) % 26

        exit += ALPH[pos]
    else:
        exit += symbol

print(exit)

pyperclip.copy(exit)
