# Simple Merge Sort with Pivoting
# The Disorganized Handyman
# By Caliber_X

# Number of runs
runs = 0

def quick_sort(start, finish):

    # Base Case to control recursion
    if start >= finish:
        print("Returning at", start)
        return

    # Get the position of pivot
    # pivot_pos = partition(start, finish)
    pivot_pos = clever_partition(start, finish)

    # Left Side (< Pivot)
    quick_sort(start, pivot_pos - 1)
    # Right Side (> Pivot)
    quick_sort(pivot_pos + 1, finish)

def partition(start, pivot_pos):
    global runs

    # Run till start reaches pivot
    while start < pivot_pos:
        # If start_val > pivot_val -> move start_val after pivot
        if lst[start] > lst[pivot_pos]:
            # Move larger value after pivot
            lst.insert(pivot_pos, lst.pop(start))
            # Number of iterations required to pop & insert -> shift the larger number to the right of pivot
            runs += pivot_pos - start
            pivot_pos -= 1
        else:
            start += 1
    print("Pivot = {} at pos {} ->  {}".format(lst[pivot_pos], pivot_pos, lst))
    return pivot_pos

# This fuction also returns the pivot point as the above function
# but the the above function pops & inserts the larger values to the right -> shifting to the left
# To decrease this time complexity,
# this function simply copies the larger or smaller values to the right or left respectively
def clever_partition(left, right):
    global runs
    pivot = lst[right]
    Done = False

    while not Done:

        # Going Right
        while not Done:
            if left == right:
                Done = True
                break
                # If left_value > pivot -> copy to right
            if lst[left] > pivot:
                runs += 1
                lst[right] = lst[left]
                right -= 1
                break
            left += 1
        print("Left = {} Right = {} [{: ^40}]  <-----".format(left, right, str(("{:>5}" * len(lst)).format(*lst))))

        # Going Left
        while not Done:
            if left == right:
                Done = True
                break
            # If Right_value < pivot -> copy to left
            if lst[right] < pivot:
                runs += 1
                lst[left] = lst[right]
                left += 1
                break
            right -= 1
        print("Left = {} Right = {} [{: ^40}]  ----->".format(left, right, str(("{:>5}" * len(lst)).format(*lst))))

    lst[left] = pivot
    print("Pivot = {} at pos {} ->  {}".format(lst[left], left, lst))
    return left


# lst = [7, 2, 1, 8, 6, 3, 5, 4]
# lst = [8, 7, 6, 5, 4, 3, 2, 1]
lst = [4, 65, 2, -31, 0, 99, 83, 782, 1]
# lst = [4, 4, 65, 2, -31, 0, 99, 83, -31, 782, 1]

print("Original List      -> ", lst)
quick_sort(0, len(lst) - 1)
print("Tot Runs =", runs)
