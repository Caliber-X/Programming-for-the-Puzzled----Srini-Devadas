# Programming for the Puzzled -- Srini Devadas
# Ex_1_2
# 2D Binary Search
# (2*n) X (2*n)
# By Caliber_X

# quadrant : 00 (upper left), 01 (upper right),
#            10 (lower left), 11 (lower right)
quadrant = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Quadrant Approach
def ex_1(lst, search_input):

    size = len(lst[0])
    # size = size//2 : size//2-1 ? size%2
    centreR = centreC = size // 2 - 1
    row, col = recursive_search(lst, size, search_input, centreR, centreC, False)
    if (row, col) == (None, None):
        print(search_input, "not found")
    else:
        print(search_input, "found at", row, ",", col)

def recursive_search(lst, size, n, centreR, centreC, quadmiss):

    # Base case for finding even at the smallest level
    if size == 2:
        for (r, c) in quadrant:
            centre_element = lst[centreR + r][centreC + c]
            # FOUND
            if n == centre_element:
                return centreR + r, centreC + c    
        return None, None
            
    # Finding quadrant less/more than number
    # Include/Exclude that quadrant in search    
    centre_element = lst[centreR][centreC]

    # FOUND
    if n == centre_element:
        return centreR, centreC
    # EXCLUDE
    if n > centre_element:
        quadmiss = True

    for (r, c) in quadrant:

        if (r, c) == (0, 0) and quadmiss == True:
            continue
            
        else:
                            
            row, col = recursive_search(lst, size // 2, n,
                        centreR + (2*r - 1) * (size // 4), centreC + (2*c - 1) * (size // 4), False)
                
            if (row, col) != (None, None):
                return row, col
                
    return row, col
    

# Row_Column Trim Traversal Approach
def ex_2(lst, search_input):

    size = len(lst[0])
    R = 0
    C = size - 1
    row, col = recursive_search_(lst, size, search_input, R, C)
    if (row, col) == (None, None):
        print(search_input, "not found")
    else:
        print(search_input, "found at", row, ",", col)

def recursive_search_(lst, size, n, R, C):

    current = lst[R][C]
    if n == current:
        return R, C
    elif n < current:
        # Base Case
        if C == 0:
            return None, None
        row, col = recursive_search_(lst, size, n, R, C - 1)
    else:
        # Base Case
        if R == size - 1 :
            return None, None
        row, col = recursive_search_(lst, size, n, R + 1, C)

    return row, col        
    



search_input = eval(input("Enter number to search: "))

# T = [[1,  4,  7, 11],
#     [ 2,  5,  8, 19],
#     [10, 14, 17, 24],
#     [18, 21, 23, 30]]

# ex_1(T, search_input)

T = [[1,  4,  7, 11, 15],
    [ 2,  5,  8, 12, 19],
    [ 3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]]

ex_2(T, search_input)

# print (T)
# _T = []
# for i in range(2,5):
#     _T.append(T[i][:4])

# print (_T)