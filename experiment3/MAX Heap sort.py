import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

start = time.perf_counter()

heap_sort(arr)

end = time.perf_counter()

print("Sorted array:", arr)
print("Execution Time:", end - start, "seconds")
print("Time Complexity:")
print("Best Case: O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case: O(n log n)")
print("Space Complexity: O(1)")


# 1. Convert the array into a Max Heap (the largest element becomes the root).
# 2. Swap the root (largest element) with the last element.
# 3. Reduce the heap size by one.
# 4. Apply heapify to restore the Max Heap property.
# 5. Repeat until the heap size becomes 1.               
