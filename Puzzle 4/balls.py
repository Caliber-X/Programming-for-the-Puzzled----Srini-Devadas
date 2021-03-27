#Programming for the Puzzled -- Srini Devadas
#Please Do Break the Crystal
#This is an interactive procedure that given n floors and d balls determines
#what floors to drop the balls from to minimize the worst-case number of
#drops required to determine the hardness coefficient of the crystal.
#The hardness coefficient will range from 0 (breaks at Floor 1) or n (does not
#break at n.
def howHardIsTheCrystal(n, d):

    #First determine the radix r
    r = 1
    while (r**d <= n):
        r = r + 1
    print('Radix chosen is', r)

    numDrops = 0
    floorNoBreak = [0] * d
    for i in range(d):
        #Begin phase i
        for j in range(r-1):
            #increment ith digit of representation
            floorNoBreak[i] += 1
            Floor = convertToDecimal(r, d, floorNoBreak)
            #Make sure you aren't higher than the highest floor
            if Floor > n:
                floorNoBreak[i] -= 1
                break
            print ('Drop ball', i+1, 'from Floor', Floor)
            yes = input('Did the ball break (yes/no)?:')
            numDrops += 1
            if yes == 'yes':
                floorNoBreak[i] -= 1
                break


    hardness = convertToDecimal(r, d, floorNoBreak)
    print('Hardness coefficient is', hardness)
    print('Total number of drops is', numDrops)

    return

def convertToDecimal(r, d, rep):
    number = 0
    for i in range(d-1):
        number = (number + rep[i]) * r
    number += rep[d-1]

    return number

    
howHardIsTheCrystal(128, 6)