def quickSort(arr):
    size = len(arr)
    stack = []

    # Dodajemy początkowy zakres (cała tablica)
    stack.append((0, size - 1))

    # Dopóki są zakresy do przetworzenia
    while stack:
        low, high = stack.pop()

        if low < high:
            # Particionujemy tablicę
            pi = partition(arr, low, high)

            # Dodajemy lewe podzadanie (jeśli istnieje)
            if pi - 1 > low:
                stack.append((low, pi - 1))

            # Dodajemy prawe podzadanie (jeśli istnieje)
            if pi + 1 < high:
                stack.append((pi + 1, high))