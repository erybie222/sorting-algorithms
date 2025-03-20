def bubbleSort(A):
    for j in range(len(A), 0, -1):
        for i in range(j-1):
            if A[i]>A[i+1]:
                A[i] , A[i+1] = A[i+1] , A[i]

    

