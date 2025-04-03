import matplotlib.pyplot as plt
from measureSort import measureTime
from random_numbers_generator import arrayGenerator, constantArrayGenerator, decreasingArrayGenerator, increasingArrayGenerator, vShapeArrayGenerator
from sorts.heap_sort import heapSort
from sorts.insertion_sort import insertionSort
from sorts.merge_sort import mergeSort
from sorts.selection_sort import selectionSort
import sys
sys.setrecursionlimit(10**5)

sizes = [7000 + i * 7000 for i in range(15)]

# Funkcja generująca wykres dla pojedynczego typu danych
def plot_grouped_algorithms(sizes, results, title, data_type):
    if data_type == 'increasing':
        # Wykres 1 – tylko Insertion Sort
        plt.figure(figsize=(14, 6))
        plt.title(f"{title} – tylko Insertion Sort", fontsize=16)
        plt.xlabel("Rozmiar tablicy", fontsize=14)
        plt.ylabel("Czas [s]", fontsize=14)
        plt.plot(sizes, results['insertion'], label='Insertion Sort', marker='o', linestyle='-', linewidth=2)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Wykres 2 – tylko Selection Sort
        plt.figure(figsize=(14, 6))
        plt.title(f"{title} – tylko Selection Sort", fontsize=16)
        plt.xlabel("Rozmiar tablicy", fontsize=14)
        plt.ylabel("Czas [s]", fontsize=14)
        plt.plot(sizes, results['selection'], label='Selection Sort', marker='s', linestyle='--', linewidth=2)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Wykres 3 – szybkie algorytmy
        plt.figure(figsize=(14, 6))
        plt.title(f"{title} – szybkie algorytmy", fontsize=16)
        plt.xlabel("Rozmiar tablicy", fontsize=14)
        plt.ylabel("Czas [s]", fontsize=14)
        plt.plot(sizes, results['heap'], label='Heap Sort', marker='^', linestyle='-.', linewidth=2)
        plt.plot(sizes, results['merge'], label='Merge Sort', marker='D', linestyle=':', linewidth=2)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        # Standardowe dwa wykresy (wolne + szybkie)
        fig, axs = plt.subplots(1, 2, figsize=(18, 7))

        # WOLNE
        axs[0].set_title(f"{title} – wolne algorytmy", fontsize=14)
        axs[0].set_xlabel("Rozmiar tablicy", fontsize=12)
        axs[0].set_ylabel("Czas [s]", fontsize=12)
        axs[0].plot(sizes, results['insertion'], label='Insertion Sort', marker='o', linestyle='-', linewidth=2)
        axs[0].plot(sizes, results['selection'], label='Selection Sort', marker='s', linestyle='--', linewidth=2)
        axs[0].legend()
        axs[0].grid(True)

        # SZYBKIE
        axs[1].set_title(f"{title} – szybkie algorytmy", fontsize=14)
        axs[1].set_xlabel("Rozmiar tablicy", fontsize=12)
        axs[1].set_ylabel("Czas [s]", fontsize=12)
        axs[1].plot(sizes, results['heap'], label='Heap Sort', marker='^', linestyle='-.', linewidth=2)
        axs[1].plot(sizes, results['merge'], label='Merge Sort', marker='D', linestyle=':', linewidth=2)
        axs[1].legend()
        axs[1].grid(True)

        plt.suptitle(f"Wykresy dla: {title}", fontsize=16)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()


data_types = ['random', 'increasing', 'decreasing', 'vshape', 'constant']
titles = ['Dane losowe', 'Dane rosnące', 'Dane malejące', 'Dane V-kształtne', 'Dane stałe']

generators = {
    'random': lambda arr, n: arr,
    'increasing': increasingArrayGenerator,
    'decreasing': decreasingArrayGenerator,
    'vshape': vShapeArrayGenerator,
    'constant': lambda arr, n: constantArrayGenerator(n, arr[0] if arr else 0)
}


for data_type, title in zip(data_types, titles):
    results = {'insertion': [], 'selection': [], 'heap': [], 'merge': []}

    for n in sizes:
        base_array = arrayGenerator(n, sizes[-1]*10)

        if data_type == 'random':
            array_to_test = base_array.copy()
        else:
            array_to_test = generators[data_type](base_array.copy(), n)

        results['insertion'].append(measureTime(array_to_test.copy(), insertionSort))
        results['selection'].append(measureTime(array_to_test.copy(), selectionSort))
        results['heap'].append(measureTime(array_to_test.copy(), heapSort))
        results['merge'].append(measureTime(array_to_test.copy(), mergeSort))

    plot_grouped_algorithms(sizes, results, title, data_type)


