# Test 1 of the crypto book


import pyperclip

CLARO = 'abcdefghijklmnopqrstuvwxyz '
CIFRADO = 'ZYXWVUTSRQPONMLKJIHGFEDCBA '

# Store the output
exit = ''

# Enter the plain text
text = input('Enter your text: ')

# Execute the cyphring
for symbol in text.lower():
    if symbol in CLARO:
        indexe = CLARO.index(symbol)

        exit += CIFRADO[indexe]

print(exit)

pyperclip.copy(exit)
