# Use brute force to crack our own crypting


# JUST COPIED IT FROM THE BOOK, BUT DID NOT WORK

import pyperclip, detectarEspanol, transColumnDesci

# Pretty self explanatory
def main():
    print('This script performs an attack on a column transposed cryptogram')
    crypto = input('Insert a cryptogram: ')
    crypto = detectarEspanol.clean_text(crypto).upper()
    possible_msg = cryptoanalysis(crypto)

    if possible_msg == None:
        print('Not cracked code')
    else:
        print('We think its this one:\n')
        print(possible_msg)
        pyperclip.copy(possible_msg)

def progress_bar(limit):
    stars = 0
    for number in range(2, limit):
        if number % (limit // 40) == 0:
            stars += 1

    print('    0%' + " " * stars + '100 %')
    print('     |' + "-" * stars + '|')
    print('Cracking em down')

def cryptoanalysis(crypto):
    print('Testing keys')
    limit = len(crypto)
    print(limit)
    progress_bar(limit)
    razones = []
    texts = []
    keys = []

    # Try ALL the keys
    for key in range(2, limit):
        desci_text = transColumDescif.descipher(crypto, key)
        spanish, coef = detectarEspanol.is_spanish(deci_text)

    if key % (limit // 40) == 0:
        print('*', end='')

    if spanish:
        r_lex = coef
        texts.append(desci_text)
        razones.append(r_lex)
        keys.append(key)

    if razones == []:
        return None

    maxim = razones.index(max(razones))
    solucion = texts [maxim]
    key = keys[max]

    print()
    print('Possible key: %s -> %s' % (key, solucion[:100]))
    print('\nPress F to pay respects')
    answer = input('> ')
    if answer.strip().upper().startswith('F'):
        return solucion

    return None


if __name__ == '__main__':
    main()
