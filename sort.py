'''

selection
bubble
insertion
merge
quick
'''

def selection_sort(arr):
    result = []
    n = len(arr)
    for _ in range(n):
        min = arr[0]
        for i in arr:
            if i < min:
                min = i
        arr.remove(min)
        result.append(min)            
    return result
'''
Tong phep toan
n + n-1 + n-2 + ... + 1
= n * (n + 1) / 2 ~ 1/2 * n^2
'''

def bubble_sort(arr):
    result = []
    n = len(arr)
    for _ in range(n):
        for i in range(n-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def insertion_sort(arr):
    def insert(ar, ele):
        for i in range(len(ar)):
            if ele < ar[i]:
                ar.insert(i, ele)
                return ar
        ar.append(ele)
        return ar
        
    result = []
    for i in arr:
        result = insert(result,i)

    return result


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr

    def merge(ar1,ar2):
        if len(ar1) == 0:
            return ar2
        if len(ar2) == 0:
            return ar1

        if ar1[0] > ar2[0]:
            return [ar2[0]] + merge(ar1, ar2[1:])
        else:
            return [ar1[0]] + merge(ar1[1:], ar2)
    
    half = int(n/2)

    x = merge_sort(arr[:half])
    y = merge_sort(arr[half:]) 
    
    return merge(x, y)

# Quick sort 

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

# array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
# quick_sort(array, 0, len(array) - 1)
# print(array)

# Counting sort

def countingSort(inputArray):
     #  I = [2, 2, 0, 6, 1, 9, 9, 7]
    # Find the maximum element in the inputArray max =9
    maxEl = max(inputArray)

    countArrayLength = maxEl+1

    # Initialize the countArray with (max+1) zeros
#    C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    countArray = [0] * countArrayLength

    # Step 1 -> Traverse the inputArray and increase 
    # the corresponding count for every element by 1

# I = [2, 2, 0, 6, 1, 9, 9, 7] # The first element is 2
#    C = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] # We increase count of 2nd element by 1
#indices: 0  1  2  3  4  5  6  7  8  9

    for el in inputArray: 
        countArray[el] += 1

#    C = [1, 1, 2, 0, 0, 0, 1, 1, 0, 2] 
#indices: 0  1  2  3  4  5  6  7  8  9

    # Step 2 -> For each element in the countArray, 
    # sum up its value with the value of the previous 
    # element, and then store that value 
    # as the value of the current element
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 

#   C = [1, 2, 4, 4, 4, 4, 5, 6, 6, 8] 
#indices: 0  1  2  3  4  5  6  7  8  9

    # Step 3 -> Calculate element position
    # based on the countArray values
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray

inputArray = [2,2,0,6,1,9,9,7]
print("Input array = ", inputArray)

sortedArray = countingSort(inputArray)
print("Counting sort result = ", sortedArray)



# ar = [12, 123, 5, 24, 35, 13, 1, 6, 2]
# x = merge_sort(ar)
# print(x)



# radix sort

def countingSortForRadix(inputArray, placeValue):
    # We can assume that the number of digits used to represent
    # all numbers on the placeValue position is not grater than 10
    countArray = [0] * 10
    inputSize = len(inputArray)

    # placeElement is the value of the current place value
    # of the current element, e.g. if the current element is
    # 123, and the place value is 10, the placeElement is
    # equal to 2
    for i in range(inputSize): 
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i-1]

    # Reconstructing the output array
    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = inputArray[i]
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1
        
    return outputArray

def radixSort(inputArray):
    # Step 1 -> Find the maximum element in the input array
    maxEl = max(inputArray)

    # Step 2 -> Find the number of digits in the `max` element
    D = 1
    while maxEl > 0:
        maxEl /= 10
        D += 1
    
    # Step 3 -> Initialize the place value to the least significant place
    placeVal = 1

    # Step 4
    outputArray = inputArray
    while D > 0:
        outputArray = countingSortForRadix(outputArray, placeVal)
        placeVal *= 10  
        D -= 1

    return outputArray
    
input = [2,20,61,997,1,619]
print(input)
sorted = radixSort(input)
print(sorted)