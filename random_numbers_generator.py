import random

def arrayGenerator(n, max_val):
    A = []
    for i in range(n):
        A.append(random.randint(0, max_val))
    return A

def increasingArrayGenerator(A):
    A.sort()
    return A

def decreasingArrayGenerator(A):
    A.sort(reverse=True)
    return A

def vShapeArrayGenerator(A, n):
    half = n // 2
    first_half = A[:half]
    second_half = A[half:]
    
    first_half.sort(reverse=True)
    second_half.sort()
    
    return first_half + second_half

def aShapeArrayGenerator(A, n):
    half = n // 2
    first_half = A[:half]
    second_half = A[half:]
    
    first_half.sort()
    second_half.sort(reverse=True)
    
    return first_half + second_half

def constantArrayGenerator(n, value=0):
    return [value for _ in range(n)]
