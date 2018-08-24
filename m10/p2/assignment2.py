'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    i = 0
    if lettersGuessed[i] in secretWord:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    str_ing = ""
    for i in secretWord:
        if i not in lettersGuessed:
            str_ing = str_ing + "_"
        else:
            str_ing = str_ing + i
    return str_ing




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alph ="abcdefghijklmnopqrstuvwxyz"
    temp = ''
    for i in alph:
        if i not in lettersGuessed:
            temp = temp + i
    return temp

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " +str(len(secretWord)) +" letters long.")
    guess = 8
    win = 0
    lettersGuessed = []
    while guess > 0 and win != 1:
        print("----------------------------------------------")
        print("Available letters", getAvailableLetters(lettersGuessed))
        p = list(input("Please guess a letter: "))
        if p[0] in lettersGuessed:
            print("Oops! You have already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        else: 
            lettersGuessed = lettersGuessed + p
            if isWordGuessed(secretWord, p) == True:
                print("Good guess!!! : ", getGuessedWord(secretWord, lettersGuessed))
                if secretWord == getGuessedWord(secretWord, lettersGuessed):
                    win = 1
            else:
                print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
                guess = guess - 1
                print("guesses left: " + str(guess))
    if win == 1:
        print("You won!!!!")
    else:
        print("Sorry, you ran out of guesses. The word was: ", secretWord)

def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)


if __name__ == "__main__":
    main()
