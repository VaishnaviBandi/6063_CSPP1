'''Assume s is a string of lower case characters.

Write a program that prints the longest
substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging.
We encourage you to work smart.
If you've spent more than a few hours on
this problem, we suggest that you move on
to a different part of the course.
If you have time, come back to this problem
after you've had a break and cleared your head.'''

def main():
    """This program prints the longest sequence of alphabets"""
STRING_INPUT = input()
STRING_A = STRING_INPUT + "!"
TEMP = ''
TEMP_1 = ''
BEG_VAL = 0
MOV_VAL = 1
LEN = len(STRING_A)
COUNT = 1
LENGTH = 1
while MOV_VAL <= LEN-1:
    COUNT = 1
    TEMP = STRING_A[BEG_VAL]
    while STRING_A[BEG_VAL] <= STRING_A[MOV_VAL] and MOV_VAL < LEN:
        COUNT = COUNT + 1
        TEMP = TEMP+STRING_A[MOV_VAL]
        BEG_VAL = MOV_VAL
        MOV_VAL = MOV_VAL + 1
    BEG_VAL = MOV_VAL
    MOV_VAL = MOV_VAL + 1
    if COUNT == LENGTH:
        TEMP_1 = TEMP_1

    if COUNT > LENGTH:
        LENGTH = COUNT
        TEMP_1 = ""
        TEMP_1 = TEMP
print(TEMP_1)

if __name__ == "__main__":
    main()
