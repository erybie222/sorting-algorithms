import matplotlib.pyplot as plt
from measureSort import measureTime
from random_numbers_generator import arrayGenerator, decreasingArrayGenerator, increasingArrayGenerator, vShapeArrayGenerator
from sorts.heap_sort import heapSort
from sorts.insertion_sort import insertionSort
from sorts.merge_sort import mergeSort
from sorts.selection_sort import selectionSort
import sys
sys.setrecursionlimit(10**5)
sizes = [2000 + i * 2000 for i in range(15)]

def plot_all_types_in_one_figure(sizes, results):
    import matplotlib.pyplot as plt

    data_types = ['random', 'increasing', 'decreasing', 'vshape']
    titles = ['Dane losowe', 'Dane rosnące', 'Dane malejące', 'Dane V-kształtne']

    fig, axs = plt.subplots(2, 2, figsize=(16, 10))  # 2 rzędy, 2 kolumny

    for i, data_type in enumerate(data_types):
        row = i // 2
        col = i % 2
        ax = axs[row][col]  # 🔥 <-- to jest poprawnie

        ax.set_title(titles[i])
        ax.set_xlabel("Rozmiar tablicy")
        ax.set_ylabel("Czas [s]")

        ax.plot(sizes, results[data_type]['insertion'], label='Insertion Sort', marker='o', linestyle='-', linewidth=2)
        ax.plot(sizes, results[data_type]['selection'], label='Selection Sort', marker='s', linestyle='--', linewidth=2)
        ax.plot(sizes, results[data_type]['heap'], label='Heap Sort', marker='^', linestyle='-.', linewidth=2)
        ax.plot(sizes, results[data_type]['merge'], label='Merge Sort', marker='D', linestyle=':', linewidth=2)

        ax.legend()
        ax.grid(True)

    plt.tight_layout()
    plt.show()
    
# Przygotuj słowniki do przechowywania czasów
results = {
    'random': {'insertion': [], 'selection': [], 'heap': [], 'merge': []},
    'increasing': {'insertion': [], 'selection': [], 'heap': [], 'merge': []},
    'decreasing': {'insertion': [], 'selection': [], 'heap': [], 'merge': []},
    'vshape': {'insertion': [], 'selection': [], 'heap': [], 'merge': []},
}

for n in sizes:
    # Generujemy dane bazowe
    base_array = arrayGenerator(n, sizes[-1]*10)

    # Tworzymy różne wersje danych
    random_array = base_array.copy()
    increasing_array = increasingArrayGenerator(base_array.copy())
    decreasing_array = decreasingArrayGenerator(base_array.copy())
    vshape_array = vShapeArrayGenerator(base_array.copy(), n)

    # Pomiar dla danych losowych
    results['random']['insertion'].append(measureTime(random_array.copy(), insertionSort))
    results['random']['selection'].append(measureTime(random_array.copy(), selectionSort))
    results['random']['heap'].append(measureTime(random_array.copy(), heapSort))
    results['random']['merge'].append(measureTime(random_array.copy(), mergeSort))

    # Pomiar dla danych rosnących
    results['increasing']['insertion'].append(measureTime(increasing_array.copy(), insertionSort))
    results['increasing']['selection'].append(measureTime(increasing_array.copy(), selectionSort))
    results['increasing']['heap'].append(measureTime(increasing_array.copy(), heapSort))
    results['increasing']['merge'].append(measureTime(increasing_array.copy(), mergeSort))

    # Pomiar dla danych malejących
    results['decreasing']['insertion'].append(measureTime(decreasing_array.copy(), insertionSort))
    results['decreasing']['selection'].append(measureTime(decreasing_array.copy(), selectionSort))
    results['decreasing']['heap'].append(measureTime(decreasing_array.copy(), heapSort))
    results['decreasing']['merge'].append(measureTime(decreasing_array.copy(), mergeSort))

    # Pomiar dla danych V-kształtnych
    results['vshape']['insertion'].append(measureTime(vshape_array.copy(), insertionSort))
    results['vshape']['selection'].append(measureTime(vshape_array.copy(), selectionSort))
    results['vshape']['heap'].append(measureTime(vshape_array.copy(), heapSort))
    results['vshape']['merge'].append(measureTime(vshape_array.copy(), mergeSort))


plot_all_types_in_one_figure(sizes, results)
