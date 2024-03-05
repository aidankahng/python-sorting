# Simple mergeSort implementation for use on a list of numerical values
# By default sorts the list in increasing order
def bubble_sort_nums(nums):
    """
    Sort nums in-place using bubble sort.
    :type nums List[int]
    :rtype nums List[int]
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# -----------------------------------------------------------------------------
# --------------------GENERALIZED BUBBLE SORT----------------------------------
# -----------------------------------------------------------------------------

# helper comparator function equivalent to ">"
def is_greater(a,b):
    return a > b

# helper comparator function comparing length of strings
def is_longer(str_a,str_b):
    return len(str_a) > len(str_b)

# Generalized mergeSort given a list along with a comparator operator
# By default sorts list in increasing order. O(n**2)
def bubble_sort(to_sort, comparator=is_greater, reverse=False):
    '''
    Sorts list to_sort in place using bubble sort
    :type to_sort list
    :type comparator function --> bool
    :type reverse bool
    :rtype to_sort list
    '''
    n = len(to_sort)
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparator(to_sort[j], to_sort[j + 1]):
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
    if reverse:
        return to_sort[::-1]
    return to_sort

# -----------------------------------------------------------------------------
# --------------------TESTING BUBBLE SORT FUNCTIONS----------------------------
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    words_test = ["bob", "john", "game", "create", "a", ""]
    print(bubble_sort([2,5,6,7,8,12,4,2.1,-20,5,6,8,89]))
    print(bubble_sort([2,5,6,7,8,12,4,2,-20,5,6,8,89], reverse=True))
    print(bubble_sort(words_test, is_longer, True))
    pass