from copy import deepcopy
def mult_matrix(m1_, m2_):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m1_[0]) != len(m2_):
        print("Error: Matrix shapes invalid for mult")
        return None
    result = []
    for i in range(len(m1_)):
        row = []
        for j in range(len(m2_[0])):
            row.append(sum([m1_[i][k]*m2_[k][j] for k in range(len(m1_[0]))]))
        result.append(row)
    return result
def add_matrix(m1_, m2_):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1_) != len(m2_) or len(m1_[0]) != len(m2_[0]):
        print("Error: Matrix shapes invalid for addition")
        return None
    result = deepcopy(m1_)
    for i in range(len(m1_)):
        for j in range(len(m1_[0])):
            result[i][j] += m2_[i][j]
    return result
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    row_, column_ = list(map(int, input() . split(',')))
    matrix = []
    for i in range(row_):
        row1 = list(map(int, input() . split(' ')))
        if len(row1) != column_:
            print("Error: Invalid input for the matrix")
            return None
        matrix.append(row1)
    return matrix
def main():
    """ main function"""
    # read matrix 1
    matrix1 = read_matrix()
    if not matrix1:
        return
    # read matrix 2
    matrix2 = read_matrix()
    if not matrix2:
        return 
    # add matrix 1 and matrix 2
    result = add_matrix(matrix1, matrix2)
    print(result)
    # multiply matrix 1 and matrix 2
    result = mult_matrix(matrix1, matrix2)
    print(result)
if __name__ == '__main__':
    main()
