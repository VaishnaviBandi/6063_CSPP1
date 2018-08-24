'''
    Document Distance - A detailed description is given in the PDF
'''
import re
from collections import Counter
import math
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    regex = re.compile('[^ a-z]')
    dict1 = dict1.lower()
    dict2 = dict2.lower()
    d1 = []
    d2 = []
    improvised1 = []
    improvised2 = []
    dict1 = dict1.split()
    dict2 = dict2.split()
    for x in dict1:
        x = x.strip('')    
    for x in dict2:
        x = x.strip('')
    for x in dict1:
        x = regex.sub("", x)
        d1.append(x)
    for x in dict2:  
        x = regex.sub("", x)
        d2.append(x)
    stopwords = load_stopwords("stopwords.txt")
    for x in d1:
        if x not in stopwords.keys():
            improvised1.append(x)
    for x in d2:
        if x not in stopwords.keys():
            improvised2.append(x)
    frequency1 = {}
    frequency1 = frequency(improvised1, improvised2)
    num_sum = 0
    for x in frequency1.values():
        num_sum = num_sum + (int(x[0]) * int(x[1]))
    by = 0
    by1 = 0
    for x in frequency1.values():
        by = by + (int(x[0]) * int(x[0]))
    by11 = math.sqrt(by)
    for x in frequency1.values():
        by1 = by1 + (int(x[1]) * int(x[1]))
    by12 = math.sqrt(by1)
    numerator = num_sum
    denominator = by11 * by12
    return numerator/denominator


def frequency(list1, list2):
    m1 = dict(Counter(list1))
    m2 = dict(Counter(list2))
    m3 = {}
    for x in m1:
        if x in m2:
            m3[x] = [m1[x], m2[x]]
        else:
            m3[x] = [m1[x], 0]
    for x in m2:
        if x not in m1:
            m3[x] = [0, m2[x]]
    return m3

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
