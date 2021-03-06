'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    """function to clean up a given string by
removing the special characters and retain
alphabets in both upper and lower case and numbers"""
    regex = re.compile('[^A-Za-z0-9]')
    new_string = ''
    for word in string:
        new_string = new_string + regex.sub("", word)
    return new_string

def main():
    """ main function calling clean_string function"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
