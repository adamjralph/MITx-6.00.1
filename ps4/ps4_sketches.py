VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
n = HAND_SIZE

SCRABBLE_LETTER_VALUES = {
    'a': 2, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
wordValues = SCRABBLE_LETTER_VALUES

# How to decide if all letters in a hand have been used?
    
hand = {'a': 1, 'p': 2, 'l': 1, 'e': 1}       
for k, v in hand.items():
    print(v)
#word = 'gersdet'
#wordValues['a']-1
#print(wordValues['a'])
#print(wordValues)