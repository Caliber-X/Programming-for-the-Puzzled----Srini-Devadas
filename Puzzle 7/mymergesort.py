# Merge Sort
# Conquer & Divide Algo
# Recursive Algo
# By Caliber_X

def mergesort(l):

    # if len(l) == 2:
    #     return [min(l), max(l)]
    # elif len(l) == 3:
    #     return sorted(l)
    if len(l) <= 3:
        return sorted(l)
    else:
        middle = len(l)//2
        left = mergesort(l[:middle])
        right = mergesort(l[middle:])
        return merge(left, right)
    
# 2 finger Algo
def merge(left, right):

    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result







inp = [23, 3, 45, 7, 6, 11, 14, 12, 2]
print(mergesort(inp))
