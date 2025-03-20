def selectionSort(A):
    for i in range(len(A)-1):
        smallest_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[smallest_index]:
                smallest_index = j
        A[i] , A[smallest_index] = A[smallest_index] , A[i]
