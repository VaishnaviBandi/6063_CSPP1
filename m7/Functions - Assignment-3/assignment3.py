"""# We can make this program run faster using a technique
introduced in lecture - bisection search!

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal



# In short:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0"""

def paying_debtoffinayear(balance_i, annual_int_rate):
    """ input : int or float
    output: returns float value"""
    frst_balance = balance_i
    monthly_int_rate = annual_int_rate / 12
    lower_payment = frst_balance / 12
    upper_payment = (frst_balance * (1 + monthly_int_rate) ** 12) / 12.0
    epsilon_x = 0.03
    while abs(balance_i) > epsilon_x:
        monthly_pay_rate = (upper_payment + lower_payment)/2
        balance_i = frst_balance
        for _ in range(12):
            ans_i = balance_i - monthly_pay_rate
            balance_i = ans_i + (ans_i * monthly_int_rate)
        if balance_i > epsilon_x:
            lower_payment = monthly_pay_rate
        elif balance_i < -epsilon_x:
            upper_payment = monthly_pay_rate
        else:
            break
    return str(round(monthly_pay_rate, 2))


def main():
    """ To find the lowest payment in an year"""
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", str(paying_debtoffinayear(data[0], data[1])))
if __name__ == "__main__":
    main()
