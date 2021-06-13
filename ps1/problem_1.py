# Assume s is a string of lowe case characters.
# Write a program that counts up the number of vowels contained in this string s . valid Vowels are:
# 'a', 'e', 'i', 'o', and 'u'. For example, if s ='azcbobobegghakl', your program should print:
# Number of vowels: 5

# As a function (incorrect)

s ='azcbobobegghakl'

#def problem(s):
#    l = list(s)
#    vowels = [x for x in l if x in 'aeiou']
#    ans = len(vowels)
#    print('Number of vowels: {}'.format(ans))

# problem(s)

ans = len([x for x in s if x in 'aeiou'])
print('Number of vowels: {}'.format(ans))

