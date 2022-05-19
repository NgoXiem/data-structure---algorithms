'''

selection
bubble
insertion
merge
quick
'''
import random


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


# Quick sort using random pivot

def partition_random(arr, left_index, right_index):
    pivot = arr[left_index]
    i = left_index + 1
    for j in range(left_index + 1, right_index):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[left_index], arr[i - 1] = arr[i - 1], arr[left_index]
    return i - 1
def quick_sort_random(arr, left, right):
    if left < right:
        pivot = random.randint(left, right - 1)
        arr[pivot], arr[left] =  arr[left], arr[pivot]
        
        pivot_index = partition_random(arr, left, right)
        quick_sort_random(
            arr, left, pivot_index
        ) 
        quick_sort_random(
            arr, pivot_index + 1, right
        ) 
    return arr

# inputArray = [2,2,0,6,1,9,9,7]
# sorted = quick_sort_random(inputArray, 0, len(inputArray))
# print(sorted)


# Counting sort

def countingSort(inputArray):
    maxEl = max(inputArray)
    countArray = [0] * ( maxEl+1)

    for i in inputArray:
        countArray[i] += 1  
  
    result = []
  
    for (index, i) in enumerate(countArray):
        result += [index] * i
    return result

# inputArray = [2,2,0,6,1,9,9,7]
# sorted = countingSort(inputArray)
# print(sorted)


# radix sort

def countingSortForRadix(inputArray, placeValue):
    countArray = [0] * 10
    inputSize = len(inputArray)
 
    for i in range(inputSize): 
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] += 1

    outputArray = []
    for (index, i) in enumerate(countArray):
            outputArray += [index] * i
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
    
# input = [2,20,61,997,1,619]
# sorted = radixSort(input)
# print(sorted)


# Tree 

class Node:
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.parent_node = data

    def print_tree(self):
        print(self.data)

 # print function
    def print_tree(self):
        # if there is no left_child then don't print
        if self.left_child:
            self.left_child.print_tree()

        # print parent_node at the center
        print(self.parent_node)

        # if there is no right_child then don't print
        if self.right_child:
            self.right_child.print_tree()
    

    def insert_number(self, input_number):
        # Compare the new value with the parent node
        if self.parent_node:
            # if input number less than parent node, then it is on the left
            if input_number < self.parent_node:
                if self.left_child is None:
                    self.left_child = Node(input_number)
                else:
                    self.left_child.insert_number(input_number)

            # if input number greater than parent node, then it is on the right
            elif input_number > self.parent_node:
                if self.right_child is None:
                    self.right_child = Node(input_number)
                else:
                    self.right_child.insert_number(input_number)
        else:
            self.parent_node = input_number
    
    # Delete in binary tree
    def minValueNode(self):
        current = self
    
        # loop down to find the leftmost leaf
        while(current.left_child is not None):
            current = current.left_child
    
        return current
    

    def deleteNode(self, node):
        # Base Case
        if self is None:
            return self
    
        if node < self.parent_node:
           self.left_child =  self.left_child.deleteNode(node)
    
      
        elif(node > self.parent_node):
           self.right_child =  self.right_child.deleteNode(node)
    
     
        else:
            # Node with only one child or no child
            if self.left_child is None:
                temp = self.right_child
                self = None
                return temp
    
            elif self.right_child is None:
                temp = self.left_child
                self = None
                return temp
    
            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(self.right_child)
    
            # Copy the inorder successor's
            # content to this node
            self.parent_node = temp.parent_node
    
            # Delete the inorder successor
            self.right_child = self.deleteNode(self.right_child, temp.node)
    
        return self

    # Search in tree
    # find_value method to compare the value with nodes
    def find_value(self, input_number):
        if input_number < self.parent_node:
            if self.left_child is None:
                return str(input_number)+" is not Found"
            return self.left_child.find_value(input_number)
            
        elif input_number > self.parent_node:
            if self.right_child is None:
                return str(input_number)+" is not found"
            return self.right_child.find_value(input_number)
            
        else:
            return str(self.parent_node) + " is found"


self = Node(1)

self.insert_number(39)
self.insert_number(79)
self.insert_number(68)
self.insert_number(75)

self.deleteNode(75)
self.print_tree()