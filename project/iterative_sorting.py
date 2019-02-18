# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


arr1 = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(selection_sort(arr1))

# TO-DO: implement the Insertion Sort function below


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        while arr[j] > arr[j + 1] and j >= 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr


arr2 = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(insertion_sort(arr2))

# STRETCH: implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr3 = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(bubble_sort(arr3))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr


arr4 = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(count_sort(arr4))


'''
Bogosort is a very inefficient sorting algo.
Its name is a portmanteau of Bogus and Sort.
It permutes the original input until the input ends up in sorted order.
A real-life example would be throwing a deck of cards in the air
and then picking them up one by one to see if they're in sorted order;
if they're not, repeat.
'''
