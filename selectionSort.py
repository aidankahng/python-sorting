# Simple selection sort on a list of numerical or string values
def selection_sort_nums(nums):
    for i in range(len(nums)-1):
        curr_smallest = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[curr_smallest]:
                curr_smallest = j
        # Swap the first unsorted element with smallest seen
        nums[i], nums[curr_smallest] = nums[curr_smallest], nums[i]
    return nums

# -----------------------------------------------------------------------------
# -------------------GENERALIZED SELECTION SORT--------------------------------
# -----------------------------------------------------------------------------
# helper comparator function equivalent to ">"
def is_greater(a,b):
    return a > b

# helper comparator function comparing length of strings
def is_longer(str_a,str_b):
    return len(str_a) > len(str_b)

def selection_sort(to_sort, comparator=is_greater, reverse=False):
    '''
    Sorts the given list in O(n^2) time using selection sort.
    :type to_sort list
    :type comparator function returns boolean
    :type reverse bool
    :returntype list
    '''
    for i in range(len(to_sort)-1):
        curr_smallest = i
        for j in range(i+1,len(to_sort)):
            if comparator(to_sort[curr_smallest], to_sort[j]):
                curr_smallest = j
        # Swap the first unsorted element with smallest seen
        to_sort[i], to_sort[curr_smallest] = to_sort[curr_smallest], to_sort[i]
    if reverse:
        return to_sort[::-1]
    return to_sort

if __name__ == "__main__":
    words_test = ["bob", "john", "game", "create", "a", ""]
    print(selection_sort([2,5,6,7,8,12,4,2.1,-20,5,6,8,89]))
    print(selection_sort([2,5,6,7,8,12,4,2.1,-20,5,6,8,89], reverse=True))
    print(selection_sort(words_test, is_longer))
