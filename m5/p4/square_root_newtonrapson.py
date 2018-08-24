"""# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991"""

def main():
    """"program to find sq root using newton-raphson method"""
    input_n = int(input())
    guess_n = input_n/2
    diff = 0.01
    while 1:
        if abs(guess_n * guess_n - input_n) >= diff:
            guess_n = ((guess_n) - ((guess_n * guess_n - input_n) / (2 * (guess_n))))
        else:
            break
    print(guess_n)

if __name__ == "__main__":
    main()
