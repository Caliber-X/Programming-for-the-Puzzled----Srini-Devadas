# Programming for the Puzzled -- Puzzle 4
# Please Do Break the Crystal
# By Caliber_X

import math

def howHardIsTheCrystal(n, d):

    # RADIX
    r = (int)(n ** (1 / d)) + 1
    print("Chosen Radix = ", r)

    # Ex 1
    # Reduction in balls if possible
    d_ = (int)(math.log(n, r)) + 1
    
    if d_ < d:
        d = d_
        print("Using", d, "balls")

    ball = 1
    drops = 0
    floornobreak = [0] * d
    interval = [0, n]

    for i in range(d):          # Phases, ith ball
        for j in range(r - 1):  # drops

            floornobreak[i] += 1
            floor = convertToDecimal(r, d, floornobreak)
            if floor > n:
                floornobreak[i] -= 1
                break
            
            # Ex 3
            print("Current Check Inteval :", interval)

            print("Drop ball", ball, "from Floor", floor)
            drops += 1

            drop_test = input("Did the ball break (Y/N)?:")
            if drop_test == 'y' or drop_test == 'Y':
                interval[1] = convertToDecimal(r, d, floornobreak) - 1
                floornobreak[i] -= 1
                ball += 1
                break
            else:
                interval[0] = convertToDecimal(r, d, floornobreak) + 1

    hardness = convertToDecimal(r, d, floornobreak)
    print("\nHardness coefficient is", hardness)
    print("Total number of drops is", drops)
    # Ex 2
    print("Balls broken = ",ball-1)

def convertToDecimal(r, d, lst):

    number = 0
    for i in range(d-1):
        number = (number + lst[i]) * r
    number += lst[d-1]

    return number

def howHardIsTheCrystal2balls(n, d):

    # k(k+1)/2 >= n

    k = (int)((math.sqrt(1 + 8 * n) - 1) / 2)

    if k * (k + 1) / 2 < n:
        k += 1

    print("At most drops = ", k)

    ball = 1
    drops = 0
    floornobreak = 0
    interval = [0, n]
    jump = k
    i = k

    # 1st Ball Drops
    while i <= n:       # Floor jumping with jump reducing by 1 each time

        print("Drop ball", ball, "from Floor", i)
        drops += 1

        drop_test = input("Did the ball break (Y/N)?:")
        if drop_test == 'y' or drop_test == 'Y':
            interval[1] = i - 1
            ball += 1
            break
        else:
            floornobreak = i
            interval[0] = i + 1

        print("Current Check Inteval :", interval)
        
        jump -= 1
        i += jump

    # 2nd Ball Drops linearly
    for i in range(interval[0], interval[1]):

        print("Drop ball", ball, "from Floor", i)
        drops += 1
        
        drop_test = input("Did the ball break (Y/N)?:")
        if drop_test == 'y' or drop_test == 'Y':
            floornobreak = i - 1
            ball += 1
        
    print("\nHardness coefficient is", floornobreak)
    print("Total number of drops is", drops)
    print("Balls broken =", ball-1)
            
    
# howHardIsTheCrystal(128, 6)
howHardIsTheCrystal2balls(100, 2)