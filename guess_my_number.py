print('Please think of a number between 0 and 100! ')

low = 0
high = 100
guessed = False

while not guessed:
    ans = (high+low)//2
    print('Is your secret number {}'.format(ans))
    print("Enter 'h' to indicate that guess is too high", end=' ')
    print("Enter 'l' to indicate the guess is too low.", end=' ')
    low_high=input("Enter 'c' to indicate I guessed correctly. ")
    if low_high == 'h' or 'l' or 'c':
        if low_high == 'l':
            low = ans
            ans = (low+high) // 2
        elif low_high == 'h':
            high = ans
            ans = (low+high) // 2
        elif low_high == 'c':
            guessed = True
        else:
            print("I'm sorry I don't understand.")
            continue
   
print('Game over. Your secret number was: {}'.format(ans))