"""Program to count the number of vowels in a string"""
STR = input("Enter the string: ")
ST = STR.lower()
COUNT = 0
for char in ST:
    if char in "aeiou":
        COUNT = COUNT + 1
print(COUNT)
