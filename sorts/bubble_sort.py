def bubbleSort(A):
    n = len(A)
    for j in range(n, 0, -1):
        swapped = False
        for i in range(j - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True
        if not swapped:
            break
