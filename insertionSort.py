# Sorts by pushing the current item down until sorted within items seen before
# Essentially sorts the first m items, and then looks at the m+1 item. Repeats until all items are sorted.
def insertion_sort_nums(nums, reverse=False):
    # Start with key as index 1, end with index len(nums)
    for i in range(1,len(nums)):
        # start a comparison loop against previous item
        # If previous item is LARGER, then SWAP
        # If swap, continue making comparisons
        # Once no swap takes place, break and go to next key index
        while nums[i] < nums[i-1] and i > 0:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1
    if reverse:
        return nums[::-1]
    return nums

if __name__ == "__main__":
    print(insertion_sort_nums([-75, -52, -47, -30, 99, 6, -60, 29, 17, -11, 55, 68, -36, 34, 18, 58, 8, -100, -8, 69, 18, 46, 68, 10, 35, -22, 99, -10, -14, 80, 55, 42, 6, 99, 44, 54, -63, 66, -1, -95, -90, -24, 83, 28, -46, -93, -55, -29, 32, 82]))