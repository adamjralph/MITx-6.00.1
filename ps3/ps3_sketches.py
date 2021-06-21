import string
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):

    alphabet = string.ascii_lowercase
    return ''.join([i for i in alphabet if i not in lettersGuessed])

print(getAvailableLetters(lettersGuessed))