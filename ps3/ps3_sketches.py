
secreWord = 'apple'
lettersGuessed = 'pe'
lettersPresent = [l.append(i) for i in secretWord if i in lettersGuessed else i.append('_ ')]