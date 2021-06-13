# Problem 3
#
# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s
# in which the letters occur in alphabetical order. For example,
# if s = 'azcbobobegghakl', then your program should print
#
# Longest substring in alphabetical order is: beggh
#
# In the case of ties, print the first substring. For example,
# if s = 'abcbcd', then your program should print
#
# Longest substring in alphabetical order is: abc
#
# Note: This problem may be challenging. We encourage you to work smart.
# If you've spent more than a few hours on this problem,
# we suggest that you move on to a different part of the course.
# If you have time, come back to this problem after you've
# had a break and cleared your head.

s = 'azcbobegghakl'

#index = 0
#sub = []
#length = 0
#while index < len(s)-1:
#    if s[index] > s[index+1]:
#        index += 1
#        continue
#    elif s[index] < s[index+1]:
#        sub.append(s[index+1])
#        if len(sub) > length:
#            length = len(sub)
#            index += 1
#        else:
#            index += 1
#            continue
#print(sub)
li = []
for a in s:
    for i in a:
        if a > i:
            li.append(s)
print(li)
    #ans = [i for i in s if i < a]

#print(ans)

# Paste your code into this box 
longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print ("Longest substring in alphabetical order is:", longest)


# iterate over the string, s
# if a letter is greater than the one that proceeded
# it add it to a list
# if the letter is lesser than it's previous
# remove it
# and end the iteration
# save the resulting list
# repeat until every letter has been compared
# the result will be a number of alphabetical lists
# compare the lists and discard all but the longest
# print the long list as human readable

a = 1
li = []
p = s[a]
sub = li.append([i for i in s if i < p])
print(li)

while
    for i in s:
        if s[a] < s[a+1]:
            li.append(s[a])
        elif !<:
            break
    if li > sub:
        final.append(li)
        li = sub
    else:
        break
