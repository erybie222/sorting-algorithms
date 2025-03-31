import random
def arrayGenerator(n):
    A = []
    for i in range(n):
        A.append(random.randint(0, 9))
    return A