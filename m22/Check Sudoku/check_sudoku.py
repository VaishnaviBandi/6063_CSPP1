'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    # def isValid(grid, i, j, e):
    #         rowOk = all([e != grid[i][x] for x in range(9)])
    #         if rowOk:
    #                 columnOk = all([e != grid[x][j] for x in range(9)])
    #                 if columnOk:
    #                         # finding the top left x,y co-ordinates of the section containing the i,j cell
    #                         secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
    #                         for x in range(secTopX, secTopX+3):
    #                                 for y in range(secTopY, secTopY+3):
    #                                         if grid[x][y] == e:
    #                                                 return False
    #                         return True
    #         return False
    ------------
    # def zip(*iterables)
    # sentinel = object()
    # iterators = [iter(it) for it in iterables]
    # while iterators:
    #     result = []
    #     for it in iterators:
    #         elem = next(it, sentinel)
    #         if elem is sentinel:
    #             return
    #         result.append(elem)
    #     return tuple(result)

    # new_row = [list(i) for i in iterables(*sudoku)]
    # for i in range(9):
    #     if sum(sudoku[i]) != 45 or sum(new_row[i]) != 45:
    #         return False
    # return True
    def check(sud):
    zippedsud = zip(*sud)

    boxedsud=[]
    for li,line in enumerate(sud):
        for box in range(3):
            if not li % 3: boxedsud.append([])    # build a new box every 3 lines
            boxedsud[box + li/3*3].extend(line[box*3:box*3+3])

    for li in range(9):
        if [x for x in [set(sud[li]), set(zippedsud[li]), set(boxedsud[li])] if x != set(range(1,10))]:
            return False
    return True


def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()