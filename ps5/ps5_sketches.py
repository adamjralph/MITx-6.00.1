import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
all_letters = lower + upper
#print(lower)
#print(upper)
dict_lower = {x: x for x in lower}
dict_upper = {x: x for x in upper}
#print(dict_lower)
#print(dict_upper)
shift_dict = {**dict_lower, **dict_upper}

print(len(shift_dict))

letters_dict = {x: x for x in all_letters}
index_list = list(range(52))
numbers_dict = dict(zip(index_list, list(shift_dict.keys())))
index_dict = dict(zip(index_list, list(shift_dict.values())))
print(letters_dict)

# shift = input('Please enter a shift amount: ')

def build_shift_dict(shift):
# input letter
    letter = input('Please enter letter: ')
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    all_letters = lower + upper
    # create dictionary that converts numbers into letters
    number_to_letter = dict(zip(range(1, 53), all_letters))
    # create dictionary that converts a letter into a number
    letter_to_number = dict(zip(all_letters, range(1, 53)))
    # return number 
    number = letter_to_number[letter]
    print(number)
    shifted_letter = number_to_letter[number+shift]
    print(shifted_letter)

# input number + shift value
# return letter

build_shift_dict(4)