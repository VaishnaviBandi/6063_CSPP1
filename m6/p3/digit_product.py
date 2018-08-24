"""
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6"""
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    num = int_input
    m_i = 1
    r_i = 1
    if num == 0:
        print("0")
    elif num < 0:
        x_i = abs(num)
        while r_i <= x_i:
            z_i = x_i % 10
            m_i = m_i * z_i
            x_i = x_i//10
        print("-" + str(m_i))
    else:
        while r_i <= num:
            z_i = num % 10
            m_i = m_i * z_i
            num = num//10
        print(m_i)

if __name__ == "__main__":
    main()
