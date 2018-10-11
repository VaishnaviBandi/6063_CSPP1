'''
Document Distance - A detailed description is given in the PDF
'''
import re
import math


def get_word_freq(list_a, list_b):
    '''
    This function takes inputs list_1 and list_b as 2 lists
    and returns a Dictionary of repeated words from each list
    '''

    for each_word in list_a:
        if each_word in FREQ_DICT and each_word not in STOP_DICT.keys():
            FREQ_DICT[each_word][0] += 1
        else:
            FREQ_DICT[each_word] = [1]
            FREQ_DICT[each_word].append(0)

    for each_word in list_b:
        if each_word in FREQ_DICT and each_word not in STOP_DICT.keys():
            FREQ_DICT[each_word][1] += 1
        else:
            FREQ_DICT[each_word] = [0, 1]
    return FREQ_DICT


def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = dict1.lower()
    dict2 = dict2.lower()
    dict1 = re.sub("[^ a-z]", '', dict1.strip())
    dict2 = re.sub("[^ a-z]", '', dict2.strip())
    # f1_list = dict1.split()
    # f2_list = dict2.split()
    new_list_1 = [each_ele for each_ele in dict1.split() if each_ele not in STOP_DICT.keys()]
    new_list_2 = [each_ele for each_ele in dict2.split() if each_ele not in STOP_DICT.keys()]
    word_freq = get_word_freq(new_list_1, new_list_2)
    num = 0
    d_1 = 0
    d_2 = 0
    for dict_key in word_freq:
        num += word_freq[dict_key][0] * word_freq[dict_key][1]
        d_1 += word_freq[dict_key][0]**2
        d_2 += word_freq[dict_key][1]**2
    return num / (math.sqrt(d_1) * math.sqrt(d_2))


def load_stopwords(filename):
    '''
    loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as my_file:
        for line in my_file:
            stopwords[line.strip()] = 0
    return stopwords


STOP_DICT = load_stopwords("stopwords.txt")
FREQ_DICT = {}


def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))


if __name__ == '__main__':
    main()