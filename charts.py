from measureSort import measureTime
from random_numbers_generator import arrayGenerator
from sorts.bubble_sort import bubbleSort
from sorts.insertion_sort import insertionSort
from sorts.selection_sort import selectionSort
n=15
X = arrayGenerator(n)
y1=measureTime(X, bubbleSort)
y2=measureTime(X, insertionSort)
y3 = measureTime(X , selectionSort)

