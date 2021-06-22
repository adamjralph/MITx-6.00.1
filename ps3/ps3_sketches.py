
lettersGuessed = ['c', 'l', 'g']
def guesses(lettersGuessed, guess):
    '''
    guess (string) single, lowercase
    Called from hangan() when a guess is made.
    Returns a list of guessed letters
    '''
    lettersGuessed.append(guess) 
    return lettersGuessed

guess = 'a'
lettersGuessed = guesses(lettersGuessed, guess)
print(lettersGuessed)

guess = 'd'
lettersGuessed = guesses(lettersGuessed, guess)
print(lettersGuessed)