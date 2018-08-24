"""# Functions | Assignment-1 - Paying Debt off in a Year

# Write a program to calculate the credit card balance after one
#year if a person only pays the minimum monthly payment required by the
# credit card company each month.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment
#and remaining balance. At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than
#two decimal digits of accuracy- so print

# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135

# So your program only prints out one thing: the remaining
balance at the end of the year in the format:
# Remaining balance: 4784.0"""

def paying_debt_off_inayear(remaining_balance, annual_interest_rate, monthly_payment_rate):
    """ function to find the remaining balance anually
    input: balance,  anunual intrest rate, monthly payment rate
    output: remaining balance"""
    month_count = 1
    while month_count < 13:
        remaining_balance = remaining_balance - (monthly_payment_rate * remaining_balance)
        remaining_balance = remaining_balance + (annual_interest_rate / 12 * remaining_balance)
        month_count = month_count + 1
    return round(remaining_balance, 2)

def main():
    """ to find the remaining balance """
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance:" + " " + str(paying_debt_off_inayear(data[0], data[1], data[2])))
if __name__ == "__main__":
    main()
