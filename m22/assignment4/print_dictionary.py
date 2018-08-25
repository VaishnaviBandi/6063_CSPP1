'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    """function to print a dictionary with the keys in sorted order"""
    dict1 = sorted(dictionary.keys())
    for word in dict1:
        print(word, '-', dictionary[word])

def main():
    """main function"""
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
