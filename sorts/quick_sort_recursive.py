
import random

def partition(array, low, high, pivot_strategy='last'):
    # Wybór indeksu pivota
    if pivot_strategy == 'first':
        pivot_index = low
    elif pivot_strategy == 'middle':
        pivot_index = (low + high) // 2
    elif pivot_strategy == 'random':
        pivot_index = random.randint(low, high)
    else:  # domyślnie 'last'
        pivot_index = high

    # Przesuń pivot na koniec
    array[pivot_index], array[high] = array[high], array[pivot_index]
    pivot = array[high]

    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSortRecursive(array, low, high, pivot_strategy='last'):
    if low < high:
        pi = partition(array, low, high, pivot_strategy)

        quickSortRecursive(array, low, pi - 1, pivot_strategy)
        quickSortRecursive(array, pi + 1, high, pivot_strategy)

