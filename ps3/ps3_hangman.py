# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/home/code/projects/MITx-6.00.1x/ps3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
lettersGuessed = []
def guesses(lettersGuessed, guess):
          '''
          guess (string) single, lowercase
          Called from hangan() when a guess is made.
          Returns a list of guessed letters
          '''
          return lettersGuessed.append(guess) 


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    lettersPresent = [i for i in lettersGuessed if i in secretWord] 
    if len(lettersPresent) == len(secretWord):
      return True
    else:
      return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ''.join([i if i in lettersGuessed else ' _ ' for i in secretWord])

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    return ''.join([i for i in alphabet if i not in lettersGuessed])  

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    numberOfGuesses = 8

    lettersGuessed = []

    while isWordGuessed(secretWord, lettersGuessed) == False:

        

        print('I am thinking of a word that is {} letters long.'.format(len(chooseWord(wordlist))))
        print('You have {} guesses left.'.format(numberOfGuesses))
        print('Available letters: {}'.format(getAvailableLetters()))
        guess = input('Please guess a letter: ')
        if guess in secretWord:

          


    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = 'eden'
hangman(secretWord)
