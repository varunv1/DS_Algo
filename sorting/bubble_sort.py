import time


def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = 0
        for k in range(0, len(arr)-1):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
                swapped = 1
        if(not swapped):
            # swapped nothing means all are sorted
            break
    return arr

def selection_sort(arr):
    # select the min and put it in the array
    for i in range(len(arr)):
        
t1 = time.time()
print(bubble_sort([5, 2, 7, 1, 9]))
t2 = time.time()
print(bubble_sort([1, 2, 3, 4, 9]))
t3 = time.time()
print((t3-t2) - (t2-t1) > 0)
# print(t3-t2)
