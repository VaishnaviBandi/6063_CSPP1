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
    while STRING_A[BEG_VAL] < STRING_A[MOV_VAL] and MOV_VAL < LEN:
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
