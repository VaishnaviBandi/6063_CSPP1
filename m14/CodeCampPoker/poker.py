'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
import collections 
def value_replace(hand):
    i = 0
    l_2 = []
    while i < len(hand):
        if hand[i][0] == 'T':
            k = hand[i][0].replace("T", "10")
            l_2.append(int(k))
        elif hand[i][0] == 'J':
            k = hand[i][0].replace("J", "11")
            l_2.append(int(k))
        elif hand[i][0] == 'Q':
            k = hand[i][0].replace("Q", "12")
            l_2.append(int(k))
        elif hand[i][0] == 'K':
            k = hand[i][0].replace("K", "13")
            l_2.append(int(k))
        elif hand[i][0] == 'A':
            k = hand[i][0].replace("A", "14")
            l_2.append(int(k))
        else:
            k = (hand[i][0])
            l_2.append(int(k))
        i = i+1
    return l_2
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    l_2 = value_replace(hand)
    l_3 = sorted(l_2)
    p_tr = 0
    k_tr = 1
    check1 = 1
    while k_tr < len(l_3) and check1 == 1:
        if l_3[k_tr]-l_3[p_tr] == 1:
            pass
        else:
            check1 = 0
        k_tr = k_tr + 1
        p_tr = p_tr + 1
    return check1 == 1

def is_flush(hand):
    '''How do we find out if the given hand is a flush?
    The hand has a list of cards represented as strings.
    Do we need both the characters in the string? No.
    The second character is good enough to determine a flush
    Think of an algorithm: given the card suite how to check if it is a flush
    Write the code for it and return True if it is a flush else return False
    '''
    is_flush_ = 1
    i = 0
    j = 1
    while j < len(hand) and is_flush_ == 1:
        if hand[i][1] != hand[j][1]:
            is_flush_ = 0
        else:
            is_flush_ = 1
        i = i + 1
        j = j + 1
    return is_flush_ == 1

def is_four_of_a_kind(hand):
    hand = sorted(hand)
    return hand[0][0] == hand[3][0] or hand[1][0] == hand[4][0]

def is_three_of_a_kind(hand):
    hand = sorted(hand)
    return hand[0][0] == hand[2][0] or hand[1][0] == hand[3][0]


def is_one_pair(hand):
    hand_ = []
    hand_ = value_replace(hand)
    #hand_1 = sorted(hand)
    dict_ = (collections.Counter(hand_))
    list_ = dict.values(dict_)
    if len(list_) == 4:
        return 1
    return 0

def is_two_pair(hand):
    hand_ = []
    hand_ = value_replace(hand)
    #hand_1 = sorted(hand)
    dict_ = collections.Counter(hand_)
    list_ = dict.values(dict_)
    if len(list_) == 3:
        return 1
    return 0


def is_full_house(hand):
    hand = sorted(hand)
    pro_1 = hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]
    pro_2 = hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]
    return(pro_1 or pro_2)

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    is_straight_ = is_straight(hand)
    is_flush_ = is_flush(hand)
    is_four_of_a_kind_ = is_four_of_a_kind(hand)
    is_three_of_a_kind_ = is_three_of_a_kind(hand)
    is_one_pair_ = is_one_pair(hand)
    is_two_pair_ = is_two_pair(hand)
    is_full_house_ = is_full_house(hand)
    if is_full_house_:
        return 6
    elif is_two_pair_:
        return 2
    elif is_one_pair_:
        return 1
    elif is_three_of_a_kind_:
        return 3
    elif is_four_of_a_kind_:
        return 7
    elif is_flush_ and is_straight_:
        return 8
    elif is_flush_:
        return 5
    elif is_straight_:
        return 4
    else:
        return 0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
