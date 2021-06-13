s = 'azcbobegghakl'
st = ''
index = 0    
while index < len(s):
    if s[index+1] > s[index]:
        st += s[index]
        index += 1
    elif s[index+1] < s[index]:
        print('cont')
        index += 1
        continue
print(st)

    


                

