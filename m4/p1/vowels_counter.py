#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels
"""contained in the string s. Valid vowels are:
'a', 'e', 'i', 'o', and 'u'. For example, if s =
'azcbobobegghakl', your program should print:"""

#Number of vowels: 5

def main():
    """Program to count the number of vowels in a string"""
STR = input()
ST = STR.lower()
COUNT = 0
for CHAR in ST:
    if CHAR in "aeiou":
        COUNT = COUNT + 1
print(COUNT)


if __name__ == "__main__":
    main()
