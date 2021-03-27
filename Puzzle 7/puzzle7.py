# Programming for the Puzzled -- Srini Devadas
# Tile that Courtyard, Please
# By Caliber_X

EMPTY = -1
# quadrant of missing square: 00 (upper left), 01 (upper right),
#                             10 (lower left), 11 (lower right)
quadrant = [(0, 0), (0, 1), (1, 0), (1, 1)]

def tileMissingYard(n, rMiss, cMiss):
    
    size = 2 ** n
    yard = [[EMPTY for i in range(size)] for j in range(size)]
    centreR = centreC = size // 2 - 1
    yard, piece = recursive_tile(yard, size, centreR, centreC, rMiss, cMiss, 0)
    printyard(yard)
    print("\nTotal Tiles =", piece)
    
def recursive_tile(yard, size, centreR, centreC, rMiss, cMiss, piece):
    
    # Finding quadrant of missing square or tiled
    quadmiss = ((rMiss > centreR), (cMiss > centreC))
    # print(quadmiss)

    # Putting tromino
    for (R, C) in quadrant:
        if (R, C) != quadmiss:            
            yard[centreR + R][centreC + C] = chr(piece % 26 + ord('A'))

    piece += 1
        
    # Base Case (2x2 yard)
    if size == 2:
        return yard, piece

    # printyard(yard)

    # Recursive Call
    for (r, c) in quadrant:

        if (r, c) != quadmiss:
            yard, piece = recursive_tile(yard, size // 2,
                            centreR + (2*r - 1) * (size // 4), centreC + (2*c - 1) * (size // 4),
                            centreR + r, centreC + c, piece)

        else:
            yard, piece = recursive_tile(yard, size // 2,
                            centreR + (2*r - 1) * (size // 4), centreC + (2*c - 1) * (size // 4),
                            rMiss, cMiss, piece)

        # printyard(yard)
    
    return yard, piece
    
def printyard(yard):

    for row in yard:
        for col in row:
            if col == EMPTY:
                print(' ', end='  ')
            else:
                print(col, end='  ')
        print()
        


tileMissingYard(5, 5, 6)
# tileMissingYard(4, 5, 7)