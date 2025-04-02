import matplotlib.pyplot as plt
from measureSort import measureTime
from random_numbers_generator import arrayGenerator

from sorts.bubble_sort import bubbleSort
from sorts.insertion_sort import insertionSort
from sorts.selection_sort import selectionSort




sizes = [500 + i * 1000 for i in range(15)]
times_bubble = []
times_insertion = []
times_selection = []



for n in sizes:
    X = arrayGenerator(n , sizes[-1]*10)
    times_bubble.append(measureTime(X.copy(), bubbleSort))
    times_insertion.append(measureTime(X.copy(), insertionSort))
    times_selection.append(measureTime(X.copy(), selectionSort))


# Tworzenie wykresu
plt.plot(sizes, times_bubble, label='Bubble Sort', marker='o', color='red', linewidth=2)
plt.plot(sizes, times_insertion, label='Insertion Sort', marker='s', color='green', linewidth=2)
plt.plot(sizes, times_selection, label='Selection Sort', marker='^', color='blue', linewidth=2)

plt.xlabel('Rozmiar tablicy (n)')
plt.ylabel('Czas wykonania (t[s])')
plt.title('Porównanie czasów sortowania')
plt.legend()
plt.yscale('log')
plt.grid(True)
plt.tight_layout()
plt.show()