# Programming for the Puzzled -- Puzzle 5
# Keep Those Queens Apart
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

def _8_Queens(n=8):

    # 1D List for Chessboard
    board = [-1] * n
    # Counting the total no. of solutions
    count = 0
    
    # 0
    for a in range(n):
        board[0] = a

        # 1
        for b in range(n):
            board[1] = b
            if not noConflicts(board, 1):
                continue
            
            # 2
            for c in range(n):
                board[2] = c
                if not noConflicts(board, 2):
                    continue

                # 3
                for d in range(n):
                    board[3] = d
                    if not noConflicts(board, 3):
                        continue

                    # 4
                    for e in range(n):
                        board[4] = e 
                        if not noConflicts(board, 4):
                            continue

                        # 5
                        for f in range(n):
                            board[5] = f
                            if not noConflicts(board, 5):
                                continue

                            # 6
                            for g in range(n):
                                board[6] = g
                                if not noConflicts(board, 6):
                                    continue

                                # 7
                                for h in range(n):
                                    board[7] = h
                                    if noConflicts(board, 7):
                                        print(board)
                                        count += 1

    print("Total Solutions =", count)
            
def _8_Queens_Ex_2_check(check_board, n=8):

    flag = 0
    # 1D List for Chessboard
    board = [-1] * n
    
    for a in range(n):
        board[0] = a

        for b in range(n):
            board[1] = b
            if not noConflicts(board, 1):
                continue

            for c in range(n):
                board[2] = c
                if not noConflicts(board, 2):
                    continue

                for d in range(n):
                    board[3] = d
                    if not noConflicts(board, 3):
                        continue

                    for e in range(n):
                        board[4] = e 
                        if not noConflicts(board, 4):
                            continue

                        for f in range(n):
                            board[5] = f
                            if not noConflicts(board, 5):
                                continue

                            for g in range(n):
                                board[6] = g
                                if not noConflicts(board, 6):
                                    continue

                                for h in range(n):
                                    board[7] = h
                                    if noConflicts(board, 7):
                                        if check(board, check_board, n):
                                            flag = 1
                                            print(board)
    
    if flag == 0:
        print("No solution for given set of queens")

def check(board, check_board, n):

    for i in range(n):
        if check_board[i] != -1:
            if board[i] != check_board[i]:
                return False
    return True

def _8_Queens_Ex_2_reduce(check_board, n=8):

    # 1D List for Chessboard
    board = [-1] * n
    
    for a in range(n):
        if check_board[0] != -1:
            board[0] = check_board[0]
            if a!=0:    continue                # Single run for fixed placement
        else:
            board[0] = a

        for b in range(n):
            if check_board[1] != -1:
                board[1] = check_board[1]
                if b!=0:    continue
            else:
                board[1] = b
            if not noConflicts(board, 1):
                continue

            for c in range(n):
                if check_board[2] != -1:
                    board[2] = check_board[2]
                    if c!=0:    continue
                else:
                    board[2] = c
                if not noConflicts(board, 2):
                    continue

                for d in range(n):
                    if check_board[3] != -1:
                        board[3] = check_board[3]
                        if d!=0:    continue
                    else:
                        board[3] = d
                    if not noConflicts(board, 3):
                        continue

                    for e in range(n):
                        if check_board[4] != -1:
                            board[4] = check_board[4]
                            if e!=0:    continue
                        else:
                            board[4] = e
                        if not noConflicts(board, 4):
                            continue

                        for f in range(n):
                            if check_board[5] != -1:
                                board[5] = check_board[5]
                                if f!=0:    continue
                            else:
                                board[5] = f
                            if not noConflicts(board, 5):
                                continue

                            for g in range(n):
                                if check_board[6] != -1:
                                    board[6] = check_board[6]
                                    if g!=0:    continue
                                else:
                                    board[6] = g
                                if not noConflicts(board, 6):
                                    continue

                                for h in range(n):
                                    if check_board[7] != -1:
                                        board[7] = check_board[7]
                                        if h!=0:    continue
                                    else:
                                        board[7] = h
                                    if noConflicts(board, 7):
                                        print(board)


# _8_Queens()
_8_Queens_Ex_2_check([-1, 4, -1, -1, -1, -1, -1, 0])
_8_Queens_Ex_2_reduce([-1, 4, -1, -1, -1, -1, -1, 0])