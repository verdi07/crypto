# Program that codes an entered message with the cesar method

import pyperclip # Copy to the clipboard

# Text
CLARO = 'abcdefghijklmnopqrstuvwxyz '
CIFRADO = 'ZYXWVUTSRQPONMLKJIHGFEDCBA '

# Store the output
exit = ''

# Enter the plain text
text = input('Enter your text: ')

# Execute the ciphring
for symbol in text.lower():
    if symbol in CLARO:
        indexe = CLARO.index(symbol)

        exit += CIFRADO[indexe]

print(exit)

pyperclip.copy(exit)
