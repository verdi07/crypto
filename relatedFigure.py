# Program that codes or decodes using the related figure method

# Libraries
import pyperclip, criptoTools, random

# Declare the symbols availeable in our alphabet

SYMBOLS = """ !¡"#~½¬{}·$%&/()=?¿*ç^_:;,.-'ç+`ºª[\]1234567890qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM"""

# The main function allows to select the coding or decoding mode
def main():
    mode = input('Select your mode: code a message(1) or decode a message(2): ')
    while(mode != 1 or mode != 2 or mode != 0):
        if mode == 1:
            msg = input('Enter the message you want to code')
            a = int(input('Enter your decimation constant'))
            b = int(input('Enter your displacement coefficient'))
            text = code(text, a, b)
            break

        elif mode == 2:
            text = input('Enter the message you want to decode')
            a = int(input('Enter the decimation constant')) 
            b = int(input('Enter the displacement coefficient'))
            msg = decode(text, a, b)
            break

        elif mode == 0:
            sys.exit()

        else:
            print("""That was not and option, please, enter '1' to code a message, '2' to decode a message, or '0' to quit""")
