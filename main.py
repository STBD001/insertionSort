import csv
import time
import math

# Klasa przechowująca dane ocen
class RatingData:
    def __init__(self, id, title, rating):
        self.id = id
        self.title = title
        self.rating = rating

MAX_RANKINGS = 10000000

# Funkcja usuwająca puste wpisy w polu ranking
def remove_empty_ratings(arr):
    return [rating for rating in arr if rating.rating > 0]

# Funkcja zamieniająca miejscami dwa elementy w tablicy
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Funkcja dzieląca tablicę i zwracająca indeks punktu podziału
def partition(arr, low, high):
    pivot = arr[high].rating
    i = low - 1
    for j in range(low, high):
        if arr[j].rating < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1

# Implementacja algorytmu sortowania QuickSort
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Funkcja sortowania przez wstawianie
def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j].rating > key.rating:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Funkcja budująca kopiec
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left].rating > arr[largest].rating:
        largest = left
    if right < n and arr[right].rating > arr[largest].rating:
        largest = right
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, n, largest)

# Implementacja algorytmu sortowania przez kopcowanie
def heapsort(arr, low, high):
    n = high - low + 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        heapify(arr, i, 0)

# Funkcja pomocnicza do sortowania introspektywnego
def introsort_helper(arr, low, high, depth_limit):
    if high - low > 16:
        if depth_limit == 0:
            heapsort(arr, low, high)
            return
        pi = partition(arr, low, high)
        introsort_helper(arr, low, pi - 1, depth_limit - 1)
        introsort_helper(arr, pi + 1, high, depth_limit - 1)
    else:
        insertion_sort(arr, low, high)

# Implementacja algorytmu sortowania introspektywnego
def introsort(arr, n):
    depth_limit = 2 * math.log2(n)
    introsort_helper(arr, 0, n - 1, int(depth_limit))

def main():
    # Wczytanie danych z pliku
    filename = 'C:\\Users\\Dell\\Downloads\\Dane.csv'
    ratings = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Pomijanie nagłówka
        for row in csvreader:
            if len(ratings) >= MAX_RANKINGS:
                break
            id = int(row[0])
            title = row[1]
            rating = float(row[2])
            if rating <= 10.0:
                ratings.append(RatingData(id, title, rating))

    ratings = remove_empty_ratings(ratings)

    # Sortowanie ocen metodą sortowania introspektywnego

    # Dla 10 000 elementów
    start_time = time.time()
    introsort(ratings, min(10000, len(ratings)))
    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1e6
    print(f"Czas sortowania dla 10 000 elementów: {elapsed_ms:.2f} mikrosekundy")

    # Dla 100 000 elementów
    start_time = time.time()
    introsort(ratings, min(100000, len(ratings)))
    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1e6
    print(f"Czas sortowania dla 100 000 elementów: {elapsed_ms:.2f} mikrosekundy")

    # Dla 500 000 elementów
    start_time = time.time()
    introsort(ratings, min(500000, len(ratings)))
    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1e6
    print(f"Czas sortowania dla 500 000 elementów: {elapsed_ms:.2f} mikrosekundy")

    # Dla 1 000 000 elementów
    start_time = time.time()
    introsort(ratings, min(1000000, len(ratings)))
    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1e6
    print(f"Czas sortowania dla 1 000 000 elementów: {elapsed_ms:.2f} mikrosekundy")

    # Dla całej listy
    start_time = time.time()
    introsort(ratings, len(ratings))
    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1e6
    print(f"Czas sortowania dla całej listy: {elapsed_ms:.2f} mikrosekundy")

if __name__ == "__main__":
    main()
