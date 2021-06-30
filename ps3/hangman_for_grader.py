
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

    breaks = '------------'

    def letters(secretWord, lettersGuessed):
      l = [i for i in secretWord if i in lettersGuessed]
      return ''.join([i for i in l])  
    print('Welcome to the game Hangman!') 
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    print(breaks)
    while gameOn == True:
      print('You have {} guesses left.'.format(numberOfGuesses))
      print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
      guess = input('Please guess a letter: ')
      
      if guess in lettersGuessed:
        print("Oops! You've already guessed that letter: {}".format(wordSoFar))
        print(breaks)
      elif guess in secretWord:
        guesses(lettersGuessed, guess)
        wordSoFar = getGuessedWord(secretWord, lettersGuessed)
        print('Good guess: {}'.format(wordSoFar))
        print(breaks)
        if letters(secretWord, lettersGuessed) == secretWord:
          print('Congratulations, you won!')
          gameOn == False  
          break
        else:
          continue
      else:
        print('Oops! That letter is not in my word {}'.format(getGuessedWord(secretWord, lettersGuessed)))
        print(breaks)
        numberOfGuesses -= 1

