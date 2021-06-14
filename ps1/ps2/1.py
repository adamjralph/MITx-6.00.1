balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12.0
month = 0
while month < 12:
    minMonthlyPayment = balance * monthlyPaymentRate
    unpaidMonthlyBalance = balance - minMonthlyPayment
    newBalance = unpaidMonthlyBalance + monthlyInterestRate * unpaidMonthlyBalance
    balance = newBalance
    month += 1

print('Remaining balance: {}'.format(round(balance, 2)))

