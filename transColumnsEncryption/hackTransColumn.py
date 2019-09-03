# Program that uses brute force to crack the transpose column crypting

# Libraries used
import pyperclip # Copy the decoded message
import transColumnDesci as TCD # Decipher (function that decodes the cryptomessage)
import detectarEspanol as DE # is_spanish (detects if there is a correct amount of spanish words)
import math # Rounding

# Main function just asks for a message to decode and run the brute force function
def main():
    msg = input('Enter your message to decode: ') 
    multipleTry(msg)


# Clean spaces and special characters out of the english alphabet
def multipleTry(msg):
    msg = DE.clean_text(msg) 

    # Start with a lexic coeficient of 0, if a bigger appears, substitute it
    final_coef = 0

    # Loop all the number of letters in the msg and try a tranposing combination
    for i in range(1, len(msg)):
        progress_bar(i, len(msg))
        final_msg = TCD.decipher(msg, i)

        # Search in our dictionary and find the spanish words relation, if high and bigger lexic coef, get a new result 
        if(DE.is_spanish(final_msg)[0] and DE.is_spanish(final_msg)[1] > final_coef):
            final_coef = DE.is_spanish(final_msg[1])
            final_message = final_msg
    print('\n')
    print('The most probable result is:\n')
    print(final_message)
    print('\n')


# Little function to show the progress in case the message is big and gets a big time to decode
def progress_bar(it, final):
    print('    0%    |' + ('*' * math.ceil((it / final) * 30)) + ' ' * math.ceil((1 - (it / final)) * 30)  +  '|    100%', end = "\r")


if __name__ == '__main__':
    main()
