'''Assume s is a string of lower case characters.

Write a program that prints the number
of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl',
then your program should print

Number of times bob occurs is: 2'''

def main():
    """Program to find the number of 'bob' present in the given string"""
STRING = str(input())
NEW_STRING = STRING + "!"
COUNT = 0
STRING_LENGTH = len(NEW_STRING)
for x in range(0, STRING_LENGTH, 1):
    if(NEW_STRING[x] == 'b' and NEW_STRING[x+1] == 'o' and NEW_STRING[x+2] == 'b'):
        COUNT = COUNT + 1
print(COUNT)


if __name__ == "__main__":
    main()
