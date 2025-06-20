import json
import random
import time
import copy


def load_data(filepath="./Ex5/config.json"):
    with open(filepath, "r") as file:
        config = json.load(file)
    return config["data"]


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)


def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

def compare_sorts(data):
    original = copy.deepcopy(data)
    det_data = copy.deepcopy(original)
    rand_data = copy.deepcopy(original)

    print("Données de départ :", original)

    start = time.time()
    deterministic_quicksort(det_data, 0, len(det_data) - 1)
    det_time = time.time() - start
    print("\nTri déterministe :", det_data)
    print("Temps déterministe :", round(det_time, 6), "s")

    start = time.time()
    randomized_quicksort(rand_data, 0, len(rand_data) - 1)
    rand_time = time.time() - start
    print("\nTri randomisé    :", rand_data)
    print("Temps randomisé  :", round(rand_time, 6), "s")

if __name__ == "__main__":
    data = load_data()
    compare_sorts(data)
