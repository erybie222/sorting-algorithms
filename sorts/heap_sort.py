def heapSort(A):
    n = len(A)
    buildMaxHeap(A)
    
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)  


def buildMaxHeap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):  
        heapify(A, i, n)


def heapify(A, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    max_idx = i

    if left < n and A[left] > A[max_idx]:
        max_idx = left

    if right < n and A[right] > A[max_idx]:
        max_idx = right

    if max_idx != i:
        A[i], A[max_idx] = A[max_idx], A[i]
        heapify(A, max_idx, n)  
