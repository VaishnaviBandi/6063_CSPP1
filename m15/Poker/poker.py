'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''


def val_to_num(hand):
    """
    This function Converts the Face Card values to a Precedence
    """
    # new_hand = hand.copy()
    # for ele in range(5):
    #     if new_hand[ele][0] == "T":
    #         new_hand[ele] = 10
    #     elif new_hand[ele][0] == "J":
    #         new_hand[ele] = 11
    #     elif new_hand[ele][0] == "Q":
    #         new_hand[ele] = 12
    #     elif new_hand[ele][0] == "K":
    #         new_hand[ele] = 13
    #     elif new_hand[ele][0] == "A":
    #         new_hand[ele] = 14
    #     else:
    #         new_hand[ele] = int(new_hand[ele][0])
    # return new_hand
    Precedence_string = "--23456789TJQKA"
    new_hand = hand.copy()
    return sorted([Precedence_string.index(val) for val, suite in new_hand], reverse=True)


def is_royal_flush(hand):
    """
    This function returns a boolean value
    Returns : True if Hand is a Royal Flush
    """
    # print("rayal fun entered with hand", hand)
    if is_flush(hand) and is_straight(hand):
        # print("royal if passed with hand", hand)
        check_hand = val_to_num(hand)
        check_hand = sorted(check_hand)
        royal_list = [10, 11, 12, 13, 14]
        for each_val in royal_list:
            if each_val not in check_hand:
                # print("Returining royal-flush false with hand", hand)
                return False
        # print("Returining royal-flush True with hand", hand)
        return True
    return False


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

    sorted_hand = sorted(val_to_num(hand))
    # sorted_hand = [h_value for h_value in sorted_hand]
    for i in range(4):
        # print("new_hand[i]", sorted_hand[i], "new_hand [i+1]", sorted_hand[i + 1])
        if sorted_hand[i] != sorted_hand[i + 1] - 1:
            # print("Returning STratght FALSE with hand", hand)
            return False
    # print("Returning STratght TRUE with hand", hand)
    return True


def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    # print("Flush called list", hand)
    suit = hand[0][1]
    for suit_hand in range(5):
        if suit != hand[suit_hand][1]:
            # print("Returning FLUSH FALSE with hand", hand, "\n")
            return False
    # print("Returning FLUSH TRUE with hand", hand, "\n")
    return True
    # print("here", hand[0][1])


def is_four_kind(hand):
    '''
    This function returns a boolean value
    Returns : True if Hand is a Four of a Kind
    '''
    hand_copy = val_to_num(hand)
    for i in range(5):
        list_count = hand_copy.count(hand_copy[i])
        if list_count == 4:
            return True
    return False


def is_fullhouse(hand):
    '''
    This function returns a boolean value
    Returns : True if Hand is a Full house
    '''
    if is_three_kind(hand) and is_one_pair(hand):
        return True
    return False


def is_three_kind(hand):
    '''
    This function returns a boolean value
    Returns : True if Hand is a Three of a Kind
    '''
    hand_copy = val_to_num(hand)
    for i in range(5):
        list_count = hand_copy.count(hand_copy[i])
        if list_count == 3:
            return (True, hand)
    return (False, hand)


def is_one_pair(hand):
    '''
    This function returns a boolean value
    Returns : True if Hand has a pair
    '''
    hand_copy = val_to_num(hand)
    # print("printinf hand in one_pair", hand_copy)
    for i in range(5):
        list_count = hand_copy.count(hand_copy[i])
        if list_count == 2:
            return True
    return False


def is_two_pair(hand):
    '''
    This function returns a boolean value
    Returns : True if Hand has two pair
    '''
    hand_copy = val_to_num(hand)
    # print("printinf hand in two_pair", hand_copy)
    pair_count = 0
    for i in range(5):
        list_count = hand_copy.count(hand_copy[i])
        if list_count == 4:
            pair_count += 1

    if pair_count == 2:
        return True
    return False


def high_card(hand):
    '''
    This function returns a Hand value
    Returns : Returns a max value or High Card
    '''
    new_hand = val_to_num(hand)
    # print()
    return max(new_hand)


def is_kind_off(f_values, number):
    """
    determines which kind the hand is
    """
    for face in f_values:
        if f_values.count(face) == number:
            return face


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
    hand_copy = val_to_num(hand)
    rank = 0
    if is_royal_flush(hand):
        # print("Its a Royal Flush")
        rank = 9
    elif is_flush(hand) and is_straight(hand):
        # print("Its a is_flush")
        rank = 8
    elif is_four_kind(hand):
        # print("Its a is_four_kind ")
        rank = 7
    elif is_fullhouse(hand):
        # print("Its a is_fullhouse ")
        rank = 6
    elif is_flush(hand):
        # print("Its a is_flush ")
        rank = 5
    elif is_straight(hand):
        # print("Its a is_straight ")
        rank = 4
    if is_kind_off(hand_copy, 3):
        return (3, is_kind_off(hand_copy, 3), hand_copy)
    # elif is_three_kind(hand):
    #     # print("Its a is_three_kind ")
    #     # rank = 3
    #     return (rank, hand_cop)
    if is_kind_off(hand_copy, 2) and is_kind_off(sorted(hand_copy), 2):
        return (2, (is_kind_off(hand_copy, 2), is_kind_off(sorted(hand_copy), 2)), hand_copy)
    if is_kind_off(hand_copy, 2):
        return(1, is_kind_off(hand_copy, 2), hand_copy)
    # return (0, hand_copy)
    # elif is_two_pair(hand):
    #     print("Its a is_two_pair ")
    #     rank = 2
    # elif is_one_pair(hand):
    #     print("Its a is_one_pair ")
    #     rank = 1
    # print("asdasd")
    # high_val = high_card(hand)
    return (rank, hand_copy)


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
    # print(HANDS)
    # print(COUNT)
    # for x in range(COUNT):
    # ----------------------------
    # rank_dict = {rank: list(hand_rank(HANDS[rank])) for rank in range(COUNT)}
    #     #rank_dict = [list[hand_rank(HANDS[rank])] for rank in range(COUNT)]
    #     rank_list = [rank_dict[rank_][0] for rank_ in range(len(rank_dict))]
    #     high_card_list = [rank_dict[high_][1] for high_ in range(len(rank_dict))]
    #     max_rank = max(rank_list)
    #     print("max_rank=", max_rank)
    #     print("Rank list", rank_list)
    #     print(rank_dict)
    #     key = list(rank_dict.keys())
    #     max_rank_count = rank_list.count(max_count)
    #     if max_rank_count != 1:
    #         for i in range(max_rank_count):
    #             if rank_dict[i][0] == max_rank:
    #                 ans_dict = i
    #
    '''            --------------------------------
    max_rank_new = 0
    high_card_new = 0
    ans_hand = 0
    for rank_iter in range(len(rank_dict)):
        if max_rank_new < rank_dict[rank_iter][0] and high_card_new < rank_dict[rank_iter][1]:
            max_rank_new = rank_dict[rank_iter][0]
            high_card_new = rank_dict[rank_iter][1]
            ans_hand = rank_iter
    print(HANDS[ans_hand])
    '''
    # print( / key)
    # print("Count of max ranks", dict_count)

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
    # print(HANDS)

    print(' '.join(poker(HANDS)))
    # poker(HANDS)
