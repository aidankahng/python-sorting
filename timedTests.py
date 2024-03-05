import time
import random
from bubbleSort import bubble_sort_nums
from insertionSort import insertion_sort_nums
from mergeSort import merge_sort_nums
from selectionSort import selection_sort_nums


if __name__ == "__main__":

    # Generated list will have n random integer values
    n = 5000
    list_to_sort = [random.randint(-1000, 1000) for _ in range(n)]
    print("="*40)
    print(f"Running integer tests for list of size {n}:")
    # Testing for bubbleSort
    start_time = time.time()
    bubble_sort_nums(list_to_sort.copy())
    end_time = time.time()
    print(f"Elapsed time for bubbleSort:                        \t{end_time - start_time}")
    # Testing for insertionSort
    start_time = time.time()
    sorted = insertion_sort_nums(list_to_sort.copy(), True)
    end_time = time.time()
    print(f"Elapsed time for insertionSort:                     \t{end_time - start_time}")
    # insertionSort worst runtime
    start_time = time.time()
    sorted = insertion_sort_nums(sorted)
    end_time = time.time()
    print(f"Elapsed time for insertionSort (on sorted inverse): \t{end_time - start_time}")
    # Testing for mergeSort
    start_time = time.time()
    merge_sort_nums(list_to_sort.copy())
    end_time = time.time()
    print(f"Elapsed time for mergeSort:                         \t{end_time - start_time}")
    # Testing for selectionSort
    start_time = time.time()
    selection_sort_nums(list_to_sort.copy())
    end_time = time.time()
    print(f"Elapsed time for selectionSort:                     \t{end_time - start_time}")
    # Finished testing print statement
    print("="*40)
    print(f"Integer tests completed for size {n}:")