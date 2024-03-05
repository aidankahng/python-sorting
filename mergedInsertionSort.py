# Faster than pure merge_sort?
# An in-place sorting implementation
import random
import time

def insertion_sort_helper(nums, reverse=False):
    # Start with key as index 1, end with index len(nums)
    for i in range(1,len(nums)):
        # start a comparison loop against previous item
        # If previous item is LARGER, then SWAP
        # If swap, continue making comparisons
        # Once no swap takes place, break and go to next key index
        if reverse:
            while nums[i] > nums[i-1] and i > 0:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                i -= 1
        else:
            while nums[i] < nums[i-1] and i > 0:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                i -= 1

def merged_insertion_sort_nums(nums):
    '''
    mergesort implementation on a list
    splits list into smaller lists and recursively calls mergesort
    merges two sorted lists back together
    if list is less than 20 values, uses insertion sort
    '''
    if len(nums) > 20:
        sep_index = len(nums) // 2 # approximately middle index
        l_nums = nums[:sep_index] # all values up to including sep_index - 1
        r_nums = nums[sep_index:] # all other values from sep_index to end of list

        merged_insertion_sort_nums(l_nums) #sorts l_nums
        merged_insertion_sort_nums(r_nums) #sorts r_nums

        l = 0
        r = 0
        m = 0

        while l < len(l_nums) and r < len(r_nums): # as l_nums and r_nums are sorted, use comparator to merege
            if l_nums[l] <= r_nums[r]:
                nums[m] = l_nums[l]
                l += 1
            else:
                nums[m] = r_nums[r]
                r += 1
            m += 1
        while l < len(l_nums):
            nums[m] = l_nums[l]
            m += 1
            l += 1
        while r < len(r_nums):
            nums[m] = r_nums[r]
            m += 1
            r += 1
    else:
        insertion_sort_helper(nums)

if __name__ == "__main__":
    n = 100000
    test = [random.randint(-1000,1000) for _ in range(n)]
    start_time = time.time()
    merged_insertion_sort_nums(test)
    end_time = time.time()
    print(f"Elapsed time:   {end_time - start_time}")