s = 'azcbobegghakl'
#st = ''
#index = 0    
#print(len(s))
##while index < len(s)+1:
##    if s[index+1] >= s[index]:
##        st += s[index]
##        print(st)
##    elif s[index+1] < s[index]:
##        print('cont')
##        st += s[index]
##    index += 1
##print(st)
#
#while True:
#    for i in s:
#        if i > s[index+1]:
#            st = ''
#            index +=1
#        if i <= s[index+1]:
#            st += i
#            print(st)
#            index += 1
#    
#
#print(st)


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
