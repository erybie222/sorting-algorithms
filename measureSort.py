import time
def measureTime(A, sort):
    start_time = time.time()
    sort(A)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time
