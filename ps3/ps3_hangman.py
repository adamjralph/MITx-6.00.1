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
guess = ''

def guesses(lettersGuessed, guess):
          '''
          guess (string) single, lowercase
          Called from hangan() when a guess is made.
          Returns a list of guessed letters
          '''
          return lettersGuessed.append(guess)

lettersGuessed = guesses(lettersGuessed, guess)

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


gameOn = True
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

    breaks = '_ _ _ _ _ _ _ _ _ _ _ _'


    def letters(secretWord, lettersGuessed):
      l = [i for i in secretWord if i in lettersGuessed]
      return ''.join([i for i in l])  
    
    print('I am thinking of a word that is {} letters long'.format(len(secretWord)))
    print(breaks)
    print('')
    while gameOn == True:
      print('You have {} guesses left'.format(numberOfGuesses))
      print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
      guess = input('Please guess a letter: ')
      
      if guess in lettersGuessed:
        print("Oops! You've already guessed that letter: {}".format(wordSoFar))
        print(breaks)
        print('')
      elif guess in secretWord:
        guesses(lettersGuessed, guess)
        wordSoFar = getGuessedWord(secretWord, lettersGuessed)
        print('Good guess: {}'.format(wordSoFar))
        print(breaks)
        print('')
        if letters(secretWord, lettersGuessed) == secretWord:
          print('Congratualtions, you won!')
          gameOn == False  
          break
        else:
          continue
      else:
        print('Oops! That letter is not in my word {}'.format(getGuessedWord(secretWord, lettersGuessed)))
        print(breaks)
        guesses(lettersGuessed, guess)
        getAvailableLetters(lettersGuessed)
        numberOfGuesses -= 1
        if numberOfGuesses == 0:
          print('sorry, you ran out of guesses. The word was {}'.format(secretWord))
          break

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = 'e'
hangman(secretWord)

# Find out why lettersGuessed is converted to string