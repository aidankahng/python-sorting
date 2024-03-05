# Sorts by pushing the current item down until sorted within items seen before
# Essentially sorts the first m items, and then looks at the m+1 item. Repeats until all items are sorted.
def insertion_sort_nums(nums):
    # Start with key as index 1, end with index len(nums)
    for i in range(1,len(nums)):
        # start a comparison loop against previous item
        # If previous item is LARGER, then SWAP
        # If swap, continue making comparisons
        # Once no swap takes place, break and go to next key index
        while nums[i] < nums[i-1] and i > 0:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1
    return nums

print(insertion_sort_nums([2,5,6,7,8,12,4,2.1,-20,5,6,8,89]))