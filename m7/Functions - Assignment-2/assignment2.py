"""# Assignment-2 - Paying Debt off in a Year

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal"""
def paying_debtoffinayear(strt_balance, annual_int_rate):
    """ function for finding the lowest payment"""
    min_monthlypayment = 10
    temp = strt_balance
    flag = 1
    month_cnt = 0
    monthly_int_rate = (annual_int_rate) / 12.0
    if strt_balance < 0:
        flag = 0
        min_monthlypayment = 0
    while flag:
        month_cnt += 1
        monthly_unpaidbalance = (strt_balance) - (min_monthlypayment)
        strt_balance = (monthly_unpaidbalance) + (monthly_int_rate * monthly_unpaidbalance)
        if strt_balance < 0:
            flag = 0
        if month_cnt == 12 and flag != 0:
            min_monthlypayment += 10
            month_cnt = 0
            strt_balance = temp
    return min_monthlypayment

def main():
    """program to find the lowest payment using the above defined function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", paying_debtoffinayear(data[0], data[1]))
if __name__ == "__main__":
    main()
