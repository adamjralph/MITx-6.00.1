import string
shift = 4
#print(lower)
#print(upper)
#lower = [x for x in string.ascii_lowercase]
#upper = [x for x in string.ascii_uppercase]
#
#letters = lower + upper
#values = letters[shift:] + letters[:shift]
#shift_dict = dict(zip(letters, values))
#
#print(shift_dict)


# shift = input('Please enter a shift amount: ')

#def build_shift_dict(shift):
## input letter
#    letter = input('Please enter letter: ')
#    lower = string.ascii_lowercase
#    upper = string.ascii_uppercase
#    all_letters = lower + upper
#    # create dictionary that converts numbers into letters
#    number_to_letter = dict(zip(range(1, 53), all_letters))
#    # create dictionary that converts a letter into a number
#    letter_to_number = dict(zip(all_letters, range(1, 53)))
#    # return number 
#    number = letter_to_number[letter]
#    # print(number)
#
#    shifted_letter = number_to_letter[number+shift]
#    if number + shift > 52 and number > 26:
#        number -= 52
#        print(shifted_letter.upper())
#    elif number + shift > 26:
#        print(shifted_letter.lower())
#    else:
#        print(shifted_letter)
    
# input number + shift value
# return letter

# build_shift_dict(4)
class Message():

        def __init__(self, message):

            self.message = message

        def shift_dict(self, shift):

            lower = [x for x in string.ascii_lowercase]
            upper = [x for x in string.ascii_uppercase]

            letters = lower + upper
            values = letters[shift:] + letters[:shift]

            shift_dict = dict(zip(letters, values))

            return shift_dict 

m = Message('b')
code = m.shift_dict(4)
print(code)

