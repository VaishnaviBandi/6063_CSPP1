"""# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991"""

def main():
    """ program to find sq root using bisection method"""
    m_i = int(input())
    l_i = 0
    h_i = m_i
    e_i = 0.01
    while 1:
        mid = (l_i + h_i)/2
        if mid * mid >= m_i - e_i and mid * mid <= (m_i + e_i):
            break
        elif mid * mid > m_i:
            h_i = mid
        else:
            l_i = mid
    print(mid)

if __name__ == "__main__":
    main()
