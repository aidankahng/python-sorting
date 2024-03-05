import time
import threading
import random

# This is a joke. Please do not take this seriously
def sleep(num):
    time.sleep(num/50) #larger denominator is faster but less accurate
    print(num)

def sleep_sort(nums):
    threads = []
    for num in nums:
        thread = threading.Thread(target=sleep, args=(num,))
        threads.append(thread)
        thread.start() #start all threads at same time
    # put all the threads together after running all threads
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    test_list = [random.randint(1,10) for _ in range(20)]
    sleep_sort(test_list)