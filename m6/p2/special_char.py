'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    sum_i = ""
    for x_i in str_input:
        if x_i in "!@#$%^&*":
            sum_i = sum_i + " "
        else:
            sum_i = sum_i + x_i
    print(sum_i)


if __name__ == "__main__":
    main()
