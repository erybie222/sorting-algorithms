import matplotlib.pyplot as plt
from measureSort import measureTime
from sorts.quick_sort_recursive import quickSortRecursive
from random_numbers_generator import aShapeArrayGenerator, arrayGenerator
import sys
sys.setrecursionlimit(10**5)

sizes = [20000 + i * 20000 for i in range(15)]
times_right_pivot = []
times_mid_pivot = []
times_random_pivot = []


for n in sizes:
    X = arrayGenerator(n , sizes[-1]*10)
    AX = aShapeArrayGenerator(X.copy() ,n)
    times_right_pivot.append(measureTime(AX.copy(), lambda arr: quickSortRecursive(arr, 0, len(arr) - 1, 'last')))
    times_mid_pivot.append(measureTime(AX.copy(), lambda arr: quickSortRecursive(arr, 0, len(arr) - 1, 'middle')))
    times_random_pivot.append(measureTime(AX.copy(), lambda arr: quickSortRecursive(arr, 0, len(arr) - 1, 'random')))



# Tworzenie wykresu
plt.plot(sizes, times_right_pivot, label='Right pivot', color='red', marker='o', linewidth=2, markersize=6)
plt.plot(sizes, times_mid_pivot, label='Middle pivot', color='green', marker='s', linewidth=2, markersize=6)
plt.plot(sizes, times_random_pivot, label='Random Pivot', color='blue', marker='^', linewidth=2, markersize=6)

plt.xlabel('Rozmiar tablicy (n)')
plt.ylabel('Czas wykonania (t[s])')
plt.title('Porównanie czasów sortowania Quick Sort w zależności od wyboru pivota')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()