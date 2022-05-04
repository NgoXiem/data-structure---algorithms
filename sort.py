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


ar = [12, 123, 5, 24, 35, 13, 1, 6, 2]
x = merge_sort(ar)
print(x)