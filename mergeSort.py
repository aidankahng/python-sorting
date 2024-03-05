#merge sort on an array of values
def merge_sort_nums(nums):
    '''
    mergesort implementation on a list
    splits list into smaller lists and recursively calls mergesort
    merges two sorted lists back together
    '''
    if len(nums) > 1:
        sep_index = len(nums) // 2 # approximately middle index
        l_nums = nums[:sep_index] # all values up to including sep_index - 1
        r_nums = nums[sep_index:] # all other values from sep_index to end of list

        merge_sort_nums(l_nums) #sorts l_nums
        merge_sort_nums(r_nums) #sorts r_nums

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


if __name__ == "__main__":
    merge_sort_nums([-75, -52, -47, -30, 99, 6, -60, 29, 17, -11, 55, 68, -36, 34, 18, 58, 8, -100, -8, 69, 18, 46, 68, 10, 35, -22, 99, -10, -14, 80, 55, 42, 6, 99, 44, 54, -63, 66, -1, -95, -90, -24, 83, 28, -46, -93, -55, -29, 32, 82])