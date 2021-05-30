# Simple Merge Sort with Pivoting
# The Disorganized Handyman
# # By Caliber_X

# Number of runs
runs = 0

def quick_sort(start, finish):

    # Base Case to control recursion
    if start >= finish:
        print("Returning at", start)
        return

    # Get the position of pivot
    pivot_pos = partition(start, finish)
    
    # Left Side (< Pivot)
    quick_sort(start, pivot_pos - 1)
    # Right Side (> Pivot)
    quick_sort(pivot_pos + 1, finish)

def partition(start, pivot_pos):
    global runs
    
    # Run till start reaches pivot
    while start < pivot_pos:
        runs += 1
        # If start_val > pivot_val -> move start_val after pivot
        if lst[start] > lst[pivot_pos]:
            # Move larger value after pivot
            lst.insert(pivot_pos, lst.pop(start))
            pivot_pos -= 1
        else:
            start += 1
    print("Pivot = {} at pos {} ->  {}".format(lst[pivot_pos], pivot_pos, lst))
    return pivot_pos

lst = [7, 2, 1, 8, 6, 3, 5, 4]
# lst = [8, 7, 6, 5, 4, 3, 2, 1]
a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
b = [4, 4, 65, 2, -31, 0, 99, 83, -31, 782, 1]


print("Original List      -> ", lst)
quick_sort(0, len(lst) - 1)
print("Tot Runs =", runs)
