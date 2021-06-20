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