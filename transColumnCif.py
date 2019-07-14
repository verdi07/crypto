# Column tranpose cipher (for dummies)

import pyperclip

def main():
    msg = input('Enter your message: ')
    key = int(input('Enter your numeric key: '))
    msg = remove_spaces(msg)

    crypto = exit(cipher(msg,key))

    print(crypto.upper())
    pyperclip.copy(crypto.upper())

def remove_spaces(msg):
    new_msg = ''
    for symbol in msg:
        if symbol != ' ':
            new_msg += symbol
    return new_msg

def exit(crypto):
    BLOCK = 5 # Number of letter contained in each block
    text = ''
    for i in range(len(crypto)):
        if (i + 1) % BLOCK != 0:
            text += crypto[i]
        else:
            text += crypto[i] + ' '
    return text

def cipher(msg, key):
    # Each chain is a column in the list
    crypto = [''] * key
    
    # Iterate throught the columns
    for col in range(key):
        pos = col

        # In each column add the letter until we get the length of the msg
        while pos < len(msg):
            crypto[col] += msg[pos]

            pos += key

    print(''.join(crypto))
    return ''.join(crypto)


if __name__ == '__main__':
    main()

# cipher('elartedelamedicinaconsisteenentreteneralpacientemientraslanaturalezacuralaenfermedad', 7)
