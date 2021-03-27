#Programming for the Puzzled -- Srini Devadas
#Memory Serves You Well
#Take in a list of coins and find selection that maximizes sum.
#Selection obeys the constraint that adjacent coins are not selected.

#Exercise 2: Variant coin row problem where if you pick a coin you can
#pick the next one, but if you pick two in a row, you have to skip two coins.

#This procedure recursively selects coins satisfying the adjacency constraint
#The maximum value for each subproblem is stored in a dictionary memo.


def coinsVariant(row, table):

    #Base case: no coins
    if len(row) == 0:
        table[0] = 0
        return 0, table
    #base case: one coin, select it
    elif len(row) == 1:
        table[1] = row[0]
        return row[0], table

    #Recursive calls: skip
    #                 pick the coin, skip the next
    #                 pick two coins, skip two coins
    #Take the maximum and store the result

    skip = coinsVariant(row[1:], table)[0]
    pickSkip = coinsVariant(row[2:], table)[0] + row[0]
    pickPick = coinsVariant(row[4:], table)[0] + row[0] + row[1]
    result = max(skip, pickSkip, pickPick)
    table[len(row)] = result
        
    return result, table

#This procedure traces back the coin selection if it is given
#the input row of coins and the maximum values of each subproblem
#stored in the dictionary table.
#Bug fix thanks to John D. Cox.
def tracebackVariant(row, table):

    #Tracing back the coin selection
    select = []
    i = 0
    print("  Row:", row)
    print("Table:", table)
    while i < len(row):
        #print("i", i, "i+1:", i+1, "len(row)-i:", len(row)-i, "len(row)-i-4:", len(row)-i-4)
        if (table[len(row)-i] == row[i]) or\
            (table[len(row)-i] == table.get(len(row)-i-2,0) + row[i]):
            select.append(row[i])
            i += 2
        elif (table[len(row)-i] == row[i] + row[i+1]) or\
           (table[len(row)-i] == table.get(len(row)-i-4,0) + row[i] + row[i+1]):
            select.append(row[i])
            select.append(row[i+1])
            i += 4
        else:
            #Skip this coin
            i += 1
            
    print ('Input row = ', row)
    print ('Table = ', table)
    print ('Selected coins are', select, 'and sum up to', table[len(row)])
    return table[len(row)], select
    

#This procedure recursively selects coins satisfying the adjacency constraint
#The maximum value for each subproblem is stored in a dictionary memo, which
#is looked up to make sure that subproblems are not solved more than once.
def coinsVariantMemoize(row, memo):

    if len(row) == 0:
        memo[0] = 0
        return 0, memo
    elif len(row) == 1:
        memo[1] = row[0]
        return row[0], memo
    try:
        #In this case the subproblem was already solved
        return memo[len(row)], memo
    except KeyError:
        #Subproblem was not solved, need to solve it

        skip = coinsVariantMemoize(row[1:], memo)[0]
        pickSkip = coinsVariantMemoize(row[2:], memo)[0] + row[0]
        pickPick = coinsVariantMemoize(row[4:], memo)[0] + row[0] + row[1]
        result = max(skip, pickSkip, pickPick)
        memo[len(row)] = result
        
        return result, memo
    

#Iterative version of selecting coins, solving smaller subproblems first
def coinsVariantIterative(row):

    table = {}
    table[0] = 0
    table[1] = row[-1]
    table[2] = row[-1] + row[-2]
    table[3] = max(table[1] + row[-3], table[2], row[-2] + row[-3])
    for i in range(4, len(row) + 1):
        resulti = max(table[i-4] + row[1-i] + row[-i],\
                       table[i-2] + row[-i], table[i-1])
        table[i] = resulti

    return table[len(row)], table


row = [14, 3, 27, 4, 5, 15, 1]
result, memo = coinsVariant(row, {})
tracebackVariant(row, memo)
result, memo = coinsVariantMemoize(row, {})
tracebackVariant(row, memo)
result, memo = coinsVariantIterative(row)
tracebackVariant(row, memo)


lrow = [3, 15, 17, 23, 11, 3, 4, 5, 17, 23, 34, 17, 18, 14, 12, 15]
result, memo = coinsVariant(lrow, {})
tracebackVariant(lrow, memo)
result, memo = coinsVariantMemoize(lrow, {})
tracebackVariant(lrow, memo)
result, memo = coinsVariantIterative(lrow)
tracebackVariant(lrow, memo)

lrow = [3, 92, 63, 2, 79, 16, 56, 30, 75, 76, 66, 62, 11, 12, 11, 70, 10, 93, 95, 27, 100, 56, 1, 15, 50, 80, 6, 1, 37, 8, 51, 72, 33, 29, 70, 99, 42, 80, 21, 31, 25, 87, 48, 45, 66, 95, 9, 47, 89, 43, 17, 69, 88, 55, 98, 40, 78, 87, 40, 74, 6, 91]
result, memo = coinsVariantMemoize(lrow, {})
tracebackVariant(lrow, memo)
result, memo = coinsVariantIterative(lrow)
tracebackVariant(lrow, memo)



