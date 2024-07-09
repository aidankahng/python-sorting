import random
import time

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        l = [val for val in nums[1:] if val <= pivot]
        r = [val for val in nums[1:] if val > pivot]
        return quicksort(l) + [pivot] + quicksort(r)

if __name__ == "__main__":
    n = 20000
    test = [random.randint(-1000,1000) for _ in range(n)]
    start_time = time.time()
    quicksort(test)
    end_time = time.time()
    print(f"Elapsed time:   {end_time - start_time}")