# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        print(f'Loop {i}')
        print(arr)
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        print(f'smallest element: {arr[smallest_index]}')
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


animals = ['duck', 'jackal', 'hippo', 'aardvark', 'cat',
           'flamingo', 'iguana', 'giraffe', 'elephant', 'bear']

selection_sort(animals)

# TO-DO: implement the Insertion Sort function below


def insertion_sort(arr):

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
