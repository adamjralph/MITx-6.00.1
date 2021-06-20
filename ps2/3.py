# Finished but not working



balance = 999999 
annualInterestRate = 0.2
payment = 0

def monthlyInterestRate(annualInterestRate):
    '''
    Assumes annual interest rate
    a float.
    Returns monthly interes rate as float
    '''
    return annualInterestRate / 13.0

# print(f'Monthly interest rate: {monthlyInterestRate(annualInterestRate)}')

def updateBalanceMonthly(balance):
    '''
    Assumes b = Monthly uppaid balance (int or float)
    Calculates updated balance each month.
    Returns balance as int or float.
    DEPENDS ON: 
        monthyInterestRate()
        annualInterestRate
    '''
    return balance + monthlyInterestRate(annualInterestRate) * balance

def lowHighPayment(balance):

    lowerBound = round(balance / 12, 2)
    print(f'Lower: {lowerBound}')
    interestRate = monthlyInterestRate(annualInterestRate)
    upperBound = round((balance * (1 + interestRate) ** 12) / 12.0, 2)
    print(f'Upper: {upperBound}')
    lowHigh = [lowerBound, upperBound]
    return lowHigh 

def bisection(payment, balance):

    lowHigh = lowHighPayment(balance)

    if payment == 0:
        return (lowHigh[0] + lowHigh[1]) / 2
    else:
        if balance > 0:
            lowHigh[0] = payment
        elif balance < 0:
            lowHigh[1]= payment
    
    return (lowHigh[0] + lowHigh[1]) / 2

def newBalance(balance, payment):
    ''' 
    Assumes three arguments:
        1. unpaidMonthlyBalance(), an int or float
        2. balance, an int or float
        3. payment, int or float
    Subracts monthly payment from balance
    Enters result into unpaidMonthlyBalance.
    to adjust for interest.
    returns newBalance as int or float
    DEPENDS ON:
        unpaidMonthlyBalance()
    '''
    unpaidMonthlyBalance = balance - payment
    return updateBalanceMonthly(unpaidMonthlyBalance)

def findMinMonthlyPayment(balance):
    payment = 0 
    success = False
    month = 0
    adjustedBalance = balance
    newPayment = bisection(payment, balance)
    while success == False:
        if adjustedBalance <= 0:
            success = True
        else:
            while month < 12:
                updatedBalance = newBalance(adjustedBalance, payment)
                adjustedBalance = updatedBalance 
                #print(f'Month: {month} Balance: {adjustedBalance}')
                month += 1
            if adjustedBalance < 0:
                payment = bisection(newPayment, balance)
                month = 0
            elif adjustedBalance > 0:
                payment = bisection(newPayment, balance)
                month = 0
                    
        # Set success: break from loop and return new balance
    return print('Lowest Payment: ' + str(round(payment,2)))

findMinMonthlyPayment(balance)
