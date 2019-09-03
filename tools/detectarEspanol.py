# Software to detect spanish having a dictionary

# Define the alphabet
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = caps + caps.lower()


# Get the dictionary from a file in this folder
def read_dict():
    folder = open('diccionario.txt')
    spanish_words = {}
    for word in folder.read().split('\n'):
        spanish_words[word] = None
    folder.close()
    return spanish_words

SPANISH_WORDS = read_dict()

# Remove non alghabet symbols
def clean_text(msg):
    letters = []
    for symbol in msg:
        if symbol in LETTERS:
            letters.append(symbol)
    return ''.join(letters)

# Analyze if a text is in spanish, we can do this because
# the words_longer_than_four_letters - text ratio should 
# be around .7
def is_spanish(msg, r_lexica = 0.5):
    msg = clean_text(msg).upper()
    length = len(msg)
    text = ''
    for word in SPANISH_WORDS:
        if msg.find(word) != -1:
            text += word
    coef = len(text)/length
    if coef >= r_lexica:
        return True, coef
    else:
        return False, coef        
