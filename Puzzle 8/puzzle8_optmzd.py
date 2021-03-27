# Programming for the Puzzled -- Srini Devadas
# Sudoku Solver
# By Caliber_X

# Global counter
backtracks = 0
grid_traversals = 0

# Row wise transition
sectors = [ [0, 3, 0, 3], [0, 3, 3, 6], [0, 3, 6, 9],
            [3, 6, 0, 3], [3, 6, 3, 6], [3, 6, 6, 9],
            [6, 9, 0, 3], [6, 9, 3, 6], [6, 9, 6, 9]]
             

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

# #This procedure makes implications based on existing numbers on squares
def makeImplications(grid, i, j, val):

    grid[i][j] = val
    implications_made = [(i, j, val)]   # List of tuples
    global sectors
    global backtracks
    
    done = False
    #Keep going till you stop finding implications
    while not done:
        done = True

        for sect in sectors:
            
            vset = {1, 2, 3, 4, 5, 6, 7, 8, 9}  # Set
            sectinfo = []  # List of list of cordinates(x,y) & set(vset)
            
            # Sector Scanning
            # Find missing elements in sector
            # print("SECTOR Info")
            for x in range(sect[0], sect[1]):
                for y in range(sect[2], sect[3]):
                    if grid[x][y] != 0:
                        # Remove elments present in sector
                        # print(vset, grid[x][y])
                        vset.remove(grid[x][y])
                        # vset.discard(grid[x][y])
            
            # if len(vset) == 0:
            #     print("Sector Full")

            # Copy set to each empty box in sector
            for x in range(sect[0], sect[1]):
                for y in range(sect[2], sect[3]):
                    if grid[x][y] == 0:
                        sectinfo.append([x, y, vset.copy()])

            for info in sectinfo:
                
                # Horizontal Scanning
                # Find missing elements in row
                vrow = set()
                for y in range(9):
                    vrow.add(grid[info[0]][y])

                # Vertical Scanning
                # Find missing elements in column
                vcol = set()
                for x in range(9):
                    vcol.add(grid[x][info[1]])

                # info[2] = info[2].difference(vrow.union(vcol))
                info[2] -= (vrow | vcol)

                # print(info, end=' ')

                if len(info[2]) == 0:
                    # Undoing the decison, resetting implications
                    backtracks += 1
                    undoImplications(grid, implications_made)
                    implications_made = []
                    return implications_made

                if len(info[2]) == 1:
                    val = info[2].pop()
                    if isValid(grid, info[0], info[1], val):
                        grid[info[0]][info[1]] = val
                        implications_made.append((info[0], info[1], val))
                        done = False

    #         print("\n",sectinfo)
    # print("Implications = ", implications_made, end="\n\n")
    return implications_made

def undoImplications(grid, implications_made):

    for coordinates in implications_made:
        grid[coordinates[0]][coordinates[1]] = 0

def solve_Sudoku(grid, i, j):

    global backtracks

    i, j = findNextCell(grid, i, j)
       
    # Base case
    # Reached end
    if (i, j) == (-1, -1):
        return True

    for val in range(1, 10):
        if isValid(grid, i, j, val):
            # grid[i][j] = val
            implications_made = makeImplications(grid, i, j, val)

            if len(implications_made) == 0:
                continue

            if solve_Sudoku(grid, i, j):
                return True

            # Undoing the decison, resetting tree
            backtracks += 1
            # grid[i][j] = 0
            undoImplications(grid, implications_made)

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


backtracks = 0
grid_traversals = 0
grid = input
print("\nInput")
# print_Sudoku(grid)
print("Solution exists\n") if solve_Sudoku(grid, 0, 0) else print("Solution doesn't exist\n")
# print_Sudoku(grid)
print("Backtracks = ", backtracks)
print("\"Finding Next\" Grid Traversal Iterations = ", grid_traversals)

backtracks = 0
grid_traversals = 0
grid = inp2
print("\nInp2")
# print_Sudoku(grid)
print("Solution exists\n") if solve_Sudoku(grid, 0, 0) else print("Solution doesn't exist\n")
# print_Sudoku(grid)
print("Backtracks = ", backtracks)
print("\"Finding Next\" Grid Traversal Iterations = ", grid_traversals)

backtracks = 0
grid_traversals = 0
grid = inpd
print("\nInpd")
# print_Sudoku(grid)
print("Solution exists\n") if solve_Sudoku(grid, 0, 0) else print("Solution doesn't exist\n")
# print_Sudoku(grid)
print("Backtracks = ", backtracks)
print("\"Finding Next\" Grid Traversal Iterations = ", grid_traversals)

backtracks = 0
grid_traversals = 0
grid = hard
print("\nHard")
# print_Sudoku(grid)
print("Solution exists\n") if solve_Sudoku(grid, 0, 0) else print("Solution doesn't exist\n")
# print_Sudoku(grid)
print("Backtracks = ", backtracks)
print("\"Finding Next\" Grid Traversal Iterations = ", grid_traversals)

backtracks = 0
grid_traversals = 0
grid = diff
print("\nDiff")
# print_Sudoku(grid)
print("Solution exists\n") if solve_Sudoku(grid, 0, 0) else print("Solution doesn't exist\n")
# print_Sudoku(grid)
print("Backtracks = ", backtracks)
print("\"Finding Next\" Grid Traversal Iterations = ", grid_traversals)

backtracks = 0
grid_traversals = 0
grid = whs
print("\nwhs")
# print_Sudoku(grid)
print("Solution exists\n") if solve_Sudoku(grid, 0, 0) else print("Solution doesn't exist\n")
# print_Sudoku(grid)
print("Backtracks = ", backtracks)
print("\"Finding Next\" Grid Traversal Iterations = ", grid_traversals)