'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
# STOPWORDS = "stopwords.txt"

# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    
    regex = re.compile('[^a-z]')
    txt1 = []
    new_ls = []
    txt2 = []
    for string in text:
        string = string.lower().split()
        txt1.append(string)
    for string in txt1:
        k = []
        for wor in string:
            string = regex.sub("", wor)
            k.append(string)
        txt2.append(k)
    # print(txt2)
    stopwords = load_stopwords("stopwords.txt")
    for word in txt2:
        temp = []
        for wor in word:
            if wor not in stopwords.keys():
                temp.append(wor)
        new_ls.append(temp)
    return new_ls

def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    lis = word_list(docs)
    search_index = {}
    for sentence in lis:
        i = 0
        # print(len(sentence))
        # print(sentence)
        while i < len(sentence):
            line = sentence[i]
            if line in search_index.keys():
                pass
            else:
                for sublist in lis:
                    if line in sublist:
                        ind = lis.index(sublist)
                        cnt = sublist.count(line)
                        ind_cnt = (ind, cnt)
                        if line not in search_index.keys():
                            search_index[line] = [(ind_cnt)]
                        else:
                            search_index[line].append(tuple(ind_cnt))
            i = i +1
    return search_index
    # search_index = {}
    # cleanwords_list = []
    # for it_line in docs:
    #     cleanwords_list.append(word_list(it_line))
    # for line_index, it_line in enumerate(cleanwords_list):
    #     for word in it_line:
    #         if word not in STOPWORDS:
    #             if word not in search_index:
    #                 word_count = it_line.count(word)
    #                 search_index[word] = [(line_index, word_count)]
    #             elif word in search_index:
    #                 word_count = it_line.count(word)
    #                 temp_list = (line_index, word_count)
    #                 if temp_list not in search_index[word]:
    #                     search_index[word].append(temp_list)
    # return search_index
# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))
if __name__ == '__main__':
    main()
