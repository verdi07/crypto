# Decipher the column transposition

import math, pyperclip

def main():
    crypto = input('Enter the cryptogram: ')
    key = int(input('Enter the key: '))
    crypto = format_msg(crypto)

    plain_text = decipher(crypto, key)

    # Print the decoded text
    print(plain_text.lower())
    pyperclip.copy(crypto)

# Delete blanks
def format_msg(msg):
    new_msg = ''
    for symbol in msg:
        if symbol != ' ':
            new_msg += symbol

    return new_msg

def decipher(msg, key):
    matrix = [''] * key
    col = 0
    for i in range(len(msg)):
        matrix[col] += msg[i]
        if((i + 1) % math.ceil(len(msg) / key) == 0):
            col += 1
    
    final_msg = ''
    
    for i in range(math.ceil(len(msg) / key)):
        for j in range(key):
            final_msg += matrix[j][i]

    return final_msg

if __name__ == '__main__':
    main()
