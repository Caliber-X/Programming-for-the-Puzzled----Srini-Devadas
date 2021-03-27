#Programming for the Puzzled -- Srini Devadas
#Keep Those Queens Apart
#Given a 4 x 4 "chess" board, figure out how to place 4 Queens such that
#no Queen attacks another queen.
#This code uses a two-dimensional list or matrix data structure

#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current, qindex, n = 4):
    
    # #We do not need this check given how we call noConflicts()
    # #Check that there is a single 1 in the current column
    # ones = 0
    # for i in range(n):
    #     if board[i][current] == 1:
    #         ones += 1
    #         qindex = i
    # if ones > 1:
    #     return False

    #check that the row on which the current queen is only has one queen on it
    for j in range(current):
        if board[qindex][j] == 1:
            return False

    #Check the two diagonals from the current queen
    #The first loop is for the diagonal /
    #The second loop is for the diagonal \
    k = 1
    while qindex - k >= 0 and current - k >= 0:
        if board[qindex - k][current - k] == 1:
            return False
        k += 1
    k = 1
    while qindex + k < n and current - k >= 0:
        if board[qindex + k][current - k] == 1:
            return False
        k += 1

    return True 


#This procedure places 4 Queens on a board so they don't conflict
#It assumes n = 4 and won't work with other n!
def FourQueens(n=4):
    #Initialize the board to be empty
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ]

    #Place a queen a column at a time beginning with leftmost column
    for i in range(n):
        board[i][0] = 1
        for j in range(n):
            board[j][1] = 1
            if noConflicts(board, 1, j, n):
                for k in range(n):
                    board[k][2] = 1
                    if noConflicts(board, 2, k, n):
                        for m in range(n):
                            board[m][3] = 1
                            if noConflicts(board, 3, m, n):
                                print (board)
                            board[m][3] = 0
                    board[k][2] = 0
            board[j][1] = 0
        board[i][0] = 0
    # return

    # Ex 3
    print("EX 3")
    for i in range(n):
        board[i][0] = 1
        for j in range(n):
            board[j][1] = 1
            if not noConflicts(board, 1, j, n):
                board[j][1] = 0
                continue
            for k in range(n):
                board[k][2] = 1
                if not noConflicts(board, 2, k, n):
                    board[k][2] = 0
                    continue
                for m in range(n):
                    board[m][3] = 1
                    if noConflicts(board, 3, m, n):
                        print (board)
                    board[m][3] = 0
                board[k][2] = 0
            board[j][1] = 0
        board[i][0] = 0
    return


FourQueens()
