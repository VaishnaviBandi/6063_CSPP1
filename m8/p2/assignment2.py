"""# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one
number and returns the sum of digits of given number.

# This function takes in one number and returns one number."""


def sum_ofdigits(num_ber):
    '''
    input: n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if num_ber == 0:
        return 0
    return num_ber%10 + sum_ofdigits(num_ber//10)
def main():
    """ program to find the sum of the digits"""
    a_i = input()
    print(sum_ofdigits(int(a_i)))
if __name__ == "__main__":
    main()
