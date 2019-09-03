# Relative Figure Encryption cracking method
# 
#   NEED TO APPLY A FORM TO GET ALL COMBINATIONS AND 
#   PERMUTATIONS OF ALPHABETS

# Libraries
import pyperclip as PC
import tools.criptoTools as CT
import detectarEspanol as DE
import relatedFigure as RF

# Get all the characters availeable

SYMBOLS = """ º\ª1234567890!"·$%&/()=|@#~½¬{[]}?¿'¡`+'ç,.-<^*Ç;:_>·qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMł€¶ŧ←↓→øþłĸŋđðßæ«»¢µ"""

# Ask for the text to crack and show any possible crack
def main():
    text = input('Enter the text you want to decode: \n')
    decode(text)

# Find the number of different symbols in a message
def numSym(text):
    stored = ''
    counter = 0
    for symbol in text:
        if symbol not in stored:
            stored += symbol
            counter += 1
    return counter

# Generate a random alphabet with the characters in SYMBOLS
def genAlph(alph):
    for k in range(len(alph)):
        for i in range(len(alph)):
            nAlph += alph[i]
            for j in range(len(alph)):
                if j != i:
                    nAlph +=alph[j]

# Main decoding function
def decode(text):
    
