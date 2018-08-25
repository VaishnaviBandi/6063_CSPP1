'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
from collections import Counter
def tokenize(string):
    dict1 = {}
    list1 = []
    for word in string:
        if word in dict1:
            dict1[word] += 1
        elif word not in dict1:
            dict1[word] = 1
    return dict1

    # for word in string:
    #     new = string.split()
    # list1.append(new)
    # for word in list1:
    #     dict1[word] = dict1.get(word, 0) + 1
    #     # word = list1.count(word) 
    # return dict1
    # # for word in list1:
    #     if word not in dict1.keys():
    #         dict1.append(word)
    #     else:
            
def main():
    string = ''
    no_of_lines = int(input())
    for each_line in range(no_of_lines):
        string = string + (input())
        each_line += 1
    regex = re.compile('[^A-Za-z],""')
    for word in string:
        word = regex.sub("", word)
        string = string + word
    print(tokenize(string))

if __name__ == '__main__':
    main()
