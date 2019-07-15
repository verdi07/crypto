# Decipher the column transposition

import math, pyperclip # Round and copy

# Main function asks for a cryptogram with a key and deciphers it with the next functions
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
    # Get the length of the columns and round it to find if a key is possible:
    # Some keys wont be an option, since the storage of our coded message would
    # mean in the last column, more than one rows are empty (visual representation)
    #
    #                       *   *   *   *   *   *   *
    #                       *   *   *   *   *   *   *
    #                       *   *   *   *   *   *   *
    #                       *   *   *   *   *   *   *
    #                       *   *   *   *   *   *
    #                       *   *   *   *   *   *
    #                       *   *   *   *   *   *

    len_key = len(msg) / key
    rlk = math.ceil(len_key)
    
    # Complex operation, it means if the last column has more than one blank, it is not
    # a possible key
    comp_oper = (rlk - (len(msg) - (rlk * key)))

    if comp_oper > 1 and key > 2 and rlk != len_key:
        return('a')
    else:
        # Create a matrix with the columns required by the key
        matrix = [''] * key

        # Start to iterate throught the columns and add the characters
        # Column is initialized as 0, and keeps adding every time the
        # number of rows is filled  
        col = 0
        for i in range(len(msg)):
            matrix[col] += msg[i]
            if (i + 1) % math.ceil(len(msg) / key) == 0:
                col += 1

        # With the columns created, get the message picking the ordered
        # letter in each one
        final_msg = ''
        for i in range(math.floor(len(msg) / key)):
            for j in range(key):
                if (key * i + (j + 1)) <= len(msg):
                    final_msg += matrix[j][i]

        return final_msg

if __name__ == '__main__':
    main()
