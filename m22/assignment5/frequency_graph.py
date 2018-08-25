'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    """function to print a dictionary with the keys in sorted order along with the
frequency of each word"""
    for key in sorted(dictionary.items()):
        hash1 = dictionary[key] * '#'
        print(key, "-", hash1)

def main():
    """main function"""
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
