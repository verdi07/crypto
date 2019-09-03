# Program that codes or decodes using the related figure method

# Libraries
import pyperclip as PC, criptoTools as CT, random

# Declare the symbols availeable in our alphabet

SYMBOLS = """ !¡"#~½¬{}·$%&/()=?¿*ç^_:;,.-'ç+`ºª[\]1234567890qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM"""

# The main function allows to select the coding or decoding mode
def main():
    mode = int(input('Select your mode: code a message(1), decode a message(2) or quit(0) but quitting is for loosers    AND    WE      AINT        LOSERS: \n'))
    while(mode != 1 or mode != 2 or mode != 0):
        if mode == 1:
            msg = input('Enter the message you want to code:\n')
            a = int(input('Enter your decimation constant:\n'))
            b = int(input('Enter your displacement coefficient:\n'))
            text = code(msg, a, b)
            PC.copy(text)
            print('The coded text is: \n')
            print(text)
            break

        elif mode == 2:
            text = input('Enter the message you want to decode:\n')
            a = int(input('Enter the decimation constant:\n')) 
            b = int(input('Enter the displacement coefficient:\n'))
            msg = decode(text, a, b)
            PC.copy(msg)
            print('The decoded message is: \n')
            print(msg)
            break

        elif mode == 0:
            sys.exit()

        else:
            print("""That was not and option, please, enter '1' to code a message, '2' to decode a message, or '0' to quit\n""")


# Creates a random key (decimation constant and displacement coefficient)
def genKey():
    key = []
    # Random integers can be between 2 (1 would make no difference and the amount of characters)
    key.append(random.ranint(2, len(SYMBOLS)))
    key.append(random.ranint(len(SYMBOLS)))
    return key

# Checks keys are OK
def checkKeys(a, b):
    if a not in range(2, len(SYMBOLS)):
        return False
    elif b not in range(len(SYMBOLS)):
        return False
    elif CT.mcd(a,b) != 1:
        return False
    else:
        return True

# Codes a message with the related figure algorythm
def code(msg, a, b):
    textToReturn = ''
    if checkKeys(a, b):
        for symbol in msg:
            if symbol in SYMBOLS:
                textToReturn += SYMBOLS[(SYMBOLS.index(symbol) * a + b) % len(SYMBOLS)]
            else:
                textToReturn += symbol
        return textToReturn
    else:
        print('Please, enter compatible keys\n')
        return None


# Decodes a message with the related figure algorythm
def decode(text, a, b):
    msgToReturn = ''
    if checkKeys(a, b):
        invA = CT.invMod(a, len(SYMBOLS)) # Inverse module for the decode formula
        for symbol in text:
            if symbol in text:
                msgToReturn += SYMBOLS[((SYMBOLS.index(symbol) - b) * invA) % len(SYMBOLS)]
            else:
                msgToReturn += symbol
        return msgToReturn
    else:
        print('Please, enter compatible keys\n')
        return None

if __name__ == '__main__':
    main()
