#Programming for the Puzzled -- Srini Devadas
#Tile that Courtyard, Please
#Given n in a 2^n x 2^n checkyard with a missing square at position (r, c),
#find tiling of yard with trominoes (L-shaped dominoes)
#This exercise deals with 4 missing tiles and checks if
#they are in four different quadrants or any 3 of those form a tromino.

def tileFourMissingYard(n, missing):
    #Initilization
    size = 2**n
    missingquad = []
    #Filling the list with the quadrants of each of the missing tiles
    for (r,c) in missing:
        missingquad.append(2*(r >= size//2) +(c >=size//2))
    count = 0
    #Counting the number of DIFFERENT quadrants the missing tiles cover
    for i in range(4):
        if i in missingquad:
            count +=1
    #If 4 quadrants are covered then we can tile
    if count == 4:
        return True
    #Checking for L-shaped arrangement of the missing tiles
    for (r,c) in missing:
        if (((r+1,c) in missing and (r,c+1) in missing) or ((r-1,c) in missing and (r,c+1) in missing) 
        or ((r+1,c) in missing and (r,c-1) in missing) or ((r-1,c) in missing and (r,c-1)in missing)):
            return True
    return False

tileFourMissingYard(3, [(4, 4), (1, 1), (2, 1), (1, 2)])
tileFourMissingYard(3, [(4, 4), (3, 1), (2, 1), (1, 2)])
tileFourMissingYard(3, [(3, 7), (4, 4), (4, 6), (4, 7)])
