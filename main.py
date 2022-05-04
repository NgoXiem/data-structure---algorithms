import random
import time
randomlist = []

for i in range(0,10000):
    n = random.randint(1,30)
    randomlist.append(n)


start = time.time()
# call the function here
end = time.time()
print(end-start)

def bubble_sort(randomlist):
    swapped = True
    while swapped:
        swapped = False 
        for i in range(len(randomlist) -1):
            if randomlist[i] > randomlist[i+1]:
                randomlist[i], randomlist[i+1] = randomlist[i+1], randomlist[i]
                swapped = True



# start = time.time()
# bubble_sort(randomlist)
# end = time.time()
# print(round(end-start, 5))


def selection_sort(randomlist):
    for i in range(len(randomlist)):
        lowest_number_index = i
        for j in range(i+1, len(randomlist)):
            if randomlist[j] < randomlist[lowest_number_index]:
                lowest_number_index = j
        randomlist[i], randomlist[lowest_number_index] = randomlist[lowest_number_index], randomlist[i]

# start = time.time()
# selection_sort(randomlist)
# end = time.time()
# print(round(end-start, 5))


def insertion_sort(randomlist): 
    for i in range(1, len(randomlist)):
        item_to_insert = randomlist[i]
        j = i -1
        while j >= 0 and randomlist[j] > item_to_insert :
            randomlist[j+1] = randomlist[j]
            j-=1
        randomlist[j+1] = item_to_insert 

# insertion_sort(randomlist)
# print(randomlist)

def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

# merge_sort(randomlist, 0, len(randomlist) -1)
# print(randomlist)


# quick_sort
# There are different ways to do a Quick Sort partition, this implements the
# Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

# quick_sort(randomlist)
# print(randomlist)