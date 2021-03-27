#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens
#Given the dimension of a square "chess" board, call it N, find a placement
#of N queens such that no two Queens attack each other using recursive search

#Exercise 1: Pretty printing

#This procedure initializes the board to be empty, calls the recursive N-queens
#procedure and prints the returned solution
def nQueens(size):
    board = [-1] * size
    rQueens(board, 0, size)
    prettyPrint(board)

#This procedure prints the board row by row
def prettyPrint(board):

    size = len(board)
    for i in range(size):

        #Find column position of queen on this row (there will be one!)
        for j in range(size):
            if board[j] == i:
                queen = j
        row = '. ' * queen + 'Q ' + '. ' * (size - queen - 1)
        print (row)

    return


#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 


#This procedure places a queens on the board on a given column so it does
#not conflict with the existing queens, and then calls itself recursively
#to place subsequent queens till the requisite number of queens are placed
def rQueens(board, current, size):
    if (current == size):
        return True
    else:
        for i in range(size):
            board[current] = i
            if (noConflicts(board, current)):
                done = rQueens(board, current + 1, size)
                if (done):
                    return True
        return False


nQueens(20)
