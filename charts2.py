import matplotlib.pyplot as plt
from measureSort import measureTime
from random_numbers_generator import arrayGenerator

from sorts.heap_sort import heapSort
from sorts.merge_sort import mergeSort
from sorts.quick_sort_recursive import quickSortRecursive




sizes = [20000+ i * 20_000 for i in range(15)]
times_heap = []
times_merge = []
times_quick = []

for n in sizes:
    X = arrayGenerator(n , sizes[-1]*10)


    times_heap.append(measureTime(X.copy(), heapSort))
    times_merge.append(measureTime(X.copy(), mergeSort))
    A = X.copy()
    times_quick.append(measureTime(A, lambda arr: quickSortRecursive(arr, 0, len(arr) - 1)))

# Tworzenie wykresu
plt.plot(sizes, times_heap, label='Heap Sort', color='red', marker='o', linewidth=2)
plt.plot(sizes, times_merge, label='Merge Sort', color='green', marker='s', linewidth=2)
plt.plot(sizes, times_quick, label='Quick Sort', color='blue', marker='^', linewidth=2)

plt.xlabel('Rozmiar tablicy (n)')
plt.ylabel('Czas wykonania (t[s])')
plt.title('Porównanie czasów sortowania')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()