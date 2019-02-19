# STRETCH: implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        verdict = -1
        if arr[i] == target:
            verdict = i
            return verdict
    return verdict


arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(linear_search(arr, 2))
print(linear_search(arr, 4))
print(linear_search(arr, 22))

# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if target < arr[mid]:
            high = mid-1  # eliminate RHS
        elif target > arr[mid]:
            low = mid+1  # eliminate LHS
        else:
            return mid

    return -1  # not found


print(binary_search([1, 2, 3, 4, 7], 81))

# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)/2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
