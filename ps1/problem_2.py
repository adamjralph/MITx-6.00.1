# Problem 2
#
# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
#
# Number of times bob occurs is: 2
s = 'poohboobcbobbobooabobbpoboobjbobob'

index = 0
a = 0
while index < len(s)-2:
    if s[index:index+3] == 'bob':
        a += 1
    index += 1

# print(f'Number of times bob occurs is: {a}')

print('Number of times bob occurs is: {}'.format(a))
