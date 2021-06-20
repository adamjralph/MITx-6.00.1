balance = 3926
annualInterestRate = 0.2

def monthlyInterestRate(annualInterestRate):
    '''
    Assumes annual interest rate
    a float.
    Returns monthly interes rate as float
    '''
    return annualInterestRate / 12.0

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

# print(f'Update balance: {updateBalanceMonthly(balance)}')
    
def createBasePayment(balance):
    '''
    Assumes balance int or float
    Calculates a base payment to guess the number of payments
    required for findMinMonthlyPayment():
    Returns int or float
    '''
    return balance
# delete this
# payment = 100
# delete this    

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
# print(f'New balance: {newBalance(balance, payment)}')

def findMinMonthlyPayment(balance):
    '''
    Assumes balance, int or fload
    Calculates the minimum monthly payment required to pay off
    balance in 12 months.
    Checks to see if balance can be paid.
    If not increments by 0.01
    Returns newBalance as int or float.
    DEPENDS ON:
        createBasePayment()
        updateBalanceMonthly()
    '''
    success = False
    month = 0
    payment = 10
    adjustedBalance = balance
    while success == False:
        if adjustedBalance <= 0:
            success = True
        else:
            while month < 12:
                updatedBalance = newBalance(adjustedBalance, payment)
                adjustedBalance = updatedBalance 
                #print(f'Month: {month} Balance: {adjustedBalance}')
                month += 1
            if adjustedBalance > 0:
                month = 0
                payment += 10
                adjustedBalance = balance
        # Set success: break from loop and return new balance
    return print('Lowest Payment: ' + str(payment))

findMinMonthlyPayment(balance)
