# Brute force attack for the Cesar method

ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Get the cryptogram
crypto = input('Enter the cryptogram: ')

# Try every key

for key in range(len(ALPH)):
    exit = ''
    for symbol in crypto:
        if symbol in ALPH:
            pos = ALPH.index(symbol)
            exit += ALPH[(pos - key) % len(ALPH)]

        else:
            exit += symbol
    print('They key is %d , and the message is %s' % (key, exit))
