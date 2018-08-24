'''
tic tac toe
'''
def winn_er(read_m):
    '''
    to find out the winner
    '''
    return_string = ""
    if read_m[0][0] == read_m[0][1] == read_m[0][2] or\
    read_m[0][0] == read_m[1][0] == read_m[2][0] or read_m[0][0] == read_m[1][1] == read_m[2][2]:
        return_string += read_m[0][0]
    if read_m[1][0] == read_m[1][1] == read_m[1][2]:
        return_string += read_m[1][0]
    if read_m[2][0] == read_m[2][1] == read_m[2][2]:
        return_string += read_m[2][0]
    if read_m[0][2] == read_m[1][2] == read_m[2][2] or\
    read_m[2][0] == read_m[1][1] == read_m[0][2]:
        return_string += read_m[0][2]
    if read_m[0][1] == read_m[1][1] == read_m[2][1]:
        return_string += read_m[0][1]
    return return_string
def valid_input_game(read_m):
    '''
    to find out the valid input
    '''
    co_o = 0
    cou_u = 0
    coun_n = 0
    count_t = 0
    for i in range(3):
        for j in range(3):
            if read_m[i][j] == 'x':
                co_o += 1
            elif read_m[i][j] == 'o':
                cou_u += 1
            elif read_m[i][j] == '.':
                coun_n += 1
            else:
                count_t += 1
    if count_t >= 1:
        return (False, "invalid input")
    if co_o > 5 or cou_u > 5 or co_o == cou_u == coun_n == 3:
        return (False, "invalid game")
    if co_o == 5 and cou_u == 4 or co_o == 4 and cou_u == 5:
        return (False, "draw")
    return (True, "")


def read_matrix():
    '''
    to read the input
    '''
    tic_tac_toe = []
    for _ in range(3):
        lis_t = input().split(" ")
        tic_tac_toe.append(lis_t)
    return tic_tac_toe

def main():
    '''
    main function to call other functions
    '''
    read_m = read_matrix()
    tuple_output = valid_input_game(read_m)
    if tuple_output[0] is True:
        print(winn_er(read_m))
    else:
        print(tuple_output[1])
main()
