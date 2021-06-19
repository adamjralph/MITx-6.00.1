balance = 3329
annualInterestRate = 0.2

# month = 0
# while month < 12:
    # minMonthlyPayment = balance * monthlyPaymentRate
    # unpaidMonthlyBalance = balance - minMonthlyPayment
    # newBalance = unpaidMonthlyBalance + monthlyInterestRate * unpaidMonthlyBalance
    # balance = newBalance
    # month += 1
month = 0

monthlyInterestRate = annualInterestRate/12.0
monthlyPayment = 10
increment = 1

while month < 12:
    unpaidMonthlyBalance = balance - monthlyPayment
    monthlyBalance = unpaidMonthlyBalance + monthlyInterestRate * unpaidMonthlyBalance
    balance = monthlyBalance
    print(f'month: {month} balance: {balance})')
    month += 1
    if balance > 0:
        monthlyPayment += increment
    else:
        break 
# create a guess and check algorithm to find the lowest payment

print(balance)
print('Lowest Payment: {}'.format(monthlyPayment))