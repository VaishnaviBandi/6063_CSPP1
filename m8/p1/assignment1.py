"""# Exercise: Assignment-1
# Write a Python function, factorial(n),
that takes in one number and returns the
factorial of given number.This function takes
in one number and returns one number."""


def factorial(n_i):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if n_i <= 1:
        return 1

    return n_i * factorial(n_i-1)
def main():
    """ to find the factorial of a given number"""
    a_i = input()
    print(factorial(int(a_i)))
if __name__ == "__main__":
    main()
