import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
index_letters = lower + upper
#print(lower)
#print(upper)
dict_lower = {x: x for x in lower}
dict_upper = {x: x for x in upper}
#print(dict_lower)
#print(dict_upper)
shift_dict = {**dict_lower, **dict_upper}

print(len(shift_dict))

letters_dict = {x: x for x in index_letters}
index_list = list(range(52))
numbers_dict = dict(zip(index_list, list(shift_dict.keys())))
index_dict = dict(zip(index_list, list(shift_dict.values())))
print(numbers_dict)

# shift = input('Please enter a shift amount: ')
