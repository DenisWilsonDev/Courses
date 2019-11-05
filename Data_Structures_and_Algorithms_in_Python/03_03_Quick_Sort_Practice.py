"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    quicksortrec(array, 0, len(array) - 1)
    return array

def quicksortrec(array, low_index, high_index):
    if (high_index - low_index) <= 1:
        return
    pivot_index = partition(array, low_index, high_index)
    quicksortrec(array, low_index, pivot_index - 1)
    quicksortrec(array, pivot_index + 1, high_index)

def partition(array, low_index, high_index):
    element_index = low_index
    pivot_index = high_index
    while element_index < pivot_index:
        if array[element_index] < array[pivot_index]:
            element_index += 1
        elif (pivot_index - element_index) > 1:
            swap3(array, element_index, pivot_index)
            pivot_index -= 1
        else:
            swap2(array, element_index, pivot_index)
            pivot_index -= 1
    return pivot_index

def swap2(array, element_index, pivot_index):
    array[pivot_index], array[element_index] = array[element_index], array[pivot_index]

def swap3(array, element_index, pivot_index):
    array[pivot_index], array[pivot_index - 1], array[element_index] = array[element_index], array[pivot_index], array[pivot_index - 1]
    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)