# helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare
    # the first element of each when merging!
    for i in range(0, elements):
        # all elements in arrA have been merged
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        # all elements in arrB have been merged
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # next element in arrA smaller, so add to final array
        elif arrA[a] < arrB[b]:

            merged_arr[i] = arrA[a]
            a += 1
        # else, next element in arrB must be smaller, so add it to final array
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)   # merge() defined later
    return arr


arr5 = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(merge_sort(arr5))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION

def get_pivot(arr, low, high):
    mid = (low + high) // 2
    pivot = high
    if arr[low] < arr[mid]:
        if arr[mid] < arr[high]:
            pivot = mid
    elif arr[low] < arr[high]:
        pivot = low
    return pivot


def partition(arr, low, high):
    pivotIndex = get_pivot(arr, low, high)
    pivotValue = arr[pivotIndex]
    arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]
    border = low

    for i in range(low, high + 1):
        if arr[i] < pivotValue:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    arr[low], arr[border] = arr[border], arr[low]
    return border


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
    return arr


arr6 = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(quick_sort(arr6, 0, len(arr6) - 1))

# STRETCH: implement the Timsort function below
# hint: https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
