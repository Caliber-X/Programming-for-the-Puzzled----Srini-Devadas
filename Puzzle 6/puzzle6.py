# Programming for the Puzzled -- Puzzle 6
# A profusion of Queens
# 8 Queens (8x8 chessboard)
# By Caliber_X

def noConflicts(board, col):

    for i in range(col):

        # Unique in the row
        if board[col] == board[i]:
            return False
        # Diagonal Check
        if (col - i == abs(board[col] - board[i])):
            return False

    return True

def nQueens(size):

    board = [-1] * size
    rQueens(board, 0, size)

def rQueens(board, col, size):

    if col == size:
        print(board)

    else:
        for i in range(size):
            board[col] = i
            if noConflicts(board, col):
                rQueens(board, col + 1, size)

def ex_1(size):

    board = [-1] * size
    rQueens1(board, 0, size)
    pretty_print(board)

def rQueens1(board, col, size):

    if col == size:
        print(board)
        return True

    else:
        for i in range(size):
            board[col] = i
            if noConflicts(board, col):
                if rQueens1(board, col + 1, size):
                    return True
        return False

def pretty_print(board):

    size = len(board)

    for i in range(size):        
        for j in range(size):

            if i == board[j]:
                print("Q ",end='')
            else:
                print(". ", end='')
                
        print()

def ex_2(check_board):

    size = len(check_board)
    board = [-1] * size
    rQueens2(check_board, board, 0, size)
    pretty_print(board)

def rQueens2(check_board, board, col, size):

    if col == size:
        print(board)
        return True

    else:
        for i in range(size):

            if check_board[col] != -1:
                board[col] = check_board[col]
                if i!=0:    continue
            else:
                board[col] = i

            if noConflicts(board, col):
                if rQueens2(check_board, board, col + 1, size):
                    return True

        return False



# nQueens(4)
# ex_1(21)
ex_2([-1, -1, 4, -1, -1, -1, -1, 0, -1, 5])