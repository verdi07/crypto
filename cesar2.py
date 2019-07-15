# Cipher or decipher a message with the Cesar method and a selected key

import pyperclip # copy function

ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Create a blank string and add new letters to it
exit = ''

# Select the program use
mode = input('Do you want to chyper or decypher the code? (c/D)')

# Text and key
text = input('Enter the text: ')
key = int(input('Enter the key (1-25): '))

# Loop in order to code/decode the message
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

# Get the results
print(exit)

pyperclip.copy(exit)
