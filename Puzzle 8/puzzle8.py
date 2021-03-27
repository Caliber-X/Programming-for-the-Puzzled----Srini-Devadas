# Programming for the Puzzled -- Srini Devadas
# Sudoku Solver
# By Caliber_X

# Global counter
backtracks = 0
grid_traversals = 0

def print_Sudoku(grid):

    nrow = 0
    for row in grid:        
        ncol = 0
        for col in row:
            print(col, end=' ')
            ncol += 1
            if ncol % 3 == 0:
                print(' ', end=' ')            
        print()
        nrow += 1
        if nrow % 3 == 0:
            print()

# Finding Next Empty Slot to Fill
def findNextCell(grid, i, j):

    global grid_traversals
    # Reducing number of iterations
    # By starting from the previous end point + 1
    if (i, j) != (0, 0):    # First time, first box = EMPTY
        if j == len(grid) - 1:
            i += 1
            j = 0
        else:
            j += 1

    for x in range(i, len(grid)):
        for y in range(j, len(grid[0])):
            grid_traversals += 1
            if grid[x][y] == 0:
                return x, y
        if j != 0:  j = 0
                
    return - 1, -1
    
    # for x in range(0, 9):
    #     for y in range(0, 9):
    #         grid_traversals += 1
    #         if grid[x][y] == 0:
    #             return x, y
    # return -1, -1

# Checking if the value doesn't violate any Sudoku rules 
def isValid(grid, i, j, val):
    
    # Row Scan
    if all(val != grid[i][x] for x in range(9)):
        # Column Scan
        if all(val != grid[x][j] for x in range(9)):
            # Sector Scan
            # finding the top left x,y co-ordinates of
            # the section or sub-grid containing the i,j cell
            x, y = 3 * (i // 3), 3 * (j // 3)
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if grid[i][j] == val:
                        return False
            return True
    return False

def solve_Sudoku(grid, i, j):

    global backtracks

    i, j = findNextCell(grid, i, j)
       
    # Base case
    # Reached end
    if (i, j) == (-1, -1):
        return True

    for val in range(1, 10):
        if isValid(grid, i, j, val):
            grid[i][j] = val
            if solve_Sudoku(grid, i, j):
                return True
            # Undoing the decison, resetting tree
            backtracks += 1
            grid[i][j] = 0

    return False
            

input = [[5,1,7,6,0,0,0,3,4],
         [2,8,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]

inp2  = [[5,1,7,6,0,0,0,3,4],
         [0,8,9,0,0,4,0,0,0],
         [3,0,6,2,0,5,0,9,0],
         [6,0,0,0,0,0,0,1,0],
         [0,3,0,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]

inpd  = [[1,0,5,7,0,2,6,3,8],
         [2,0,0,0,0,6,0,0,5],
         [0,6,3,8,4,0,2,1,0],
         [0,5,9,2,0,1,3,8,0],
         [0,0,2,0,5,8,0,0,9],
         [7,1,0,0,3,0,5,0,2],
         [0,0,4,5,6,0,7,2,0],
         [5,0,0,0,0,4,0,6,3],
         [3,2,6,1,0,7,0,0,4]]

hard  = [[8,5,0,0,0,2,4,0,0],
         [7,2,0,0,0,0,0,0,9],
         [0,0,4,0,0,0,0,0,0],
         [0,0,0,1,0,7,0,0,2],
         [3,0,5,0,0,0,9,0,0],
         [0,4,0,0,0,0,0,0,0],
         [0,0,0,0,8,0,0,7,0],
         [0,1,7,0,0,0,0,0,0],
         [0,0,0,0,3,6,0,4,0]]

diff  = [[0,0,5,3,0,0,0,0,0],
         [8,0,0,0,0,0,0,2,0],
         [0,7,0,0,1,0,5,0,0],
         [4,0,0,0,0,5,3,0,0],
         [0,1,0,0,7,0,0,0,6],
         [0,0,3,2,0,0,0,8,0],
         [0,6,0,5,0,0,0,0,9],
         [0,0,4,0,0,0,0,3,0],
         [0,0,0,0,0,9,7,0,0]]

whs  =  [[8,0,0,0,0,0,0,0,0],
         [0,0,3,6,0,0,0,0,0],
         [0,7,0,0,9,0,2,0,0],
         [0,5,0,0,0,7,0,0,0],
         [0,0,0,0,4,5,7,0,0],
         [0,0,0,1,0,0,0,3,0],
         [0,0,1,0,0,0,0,6,8],
         [0,0,8,5,0,0,0,1,0],
         [0,9,0,0,0,0,4,0,0]]

# grid = input
# grid = inp2
# grid = inpd
grid = hard
# grid = diff
# grid = whs

# print_Sudoku(grid)
print("Solution exists\n") if solve_Sudoku(grid, 0, 0) else print("Solution doesn't exist\n")
print_Sudoku(grid)
print("Backtracks = ", backtracks)
print("\"Finding Next\" Grid Traversal Iterations = ", grid_traversals)