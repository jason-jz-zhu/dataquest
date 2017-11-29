def swap(array, pos1, pos2):
    store = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = store

def selection_sort(array):
    for i in range(len(array)):
        lowest_index = i
        for z in range(i, len(array)):
            if array[z] < array[lowest_index]:
                lowest_index = z
        swap(array, lowest_index, i)


def bubble_sort(array):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                swaps += 1


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j-1)
            j-=1
            
