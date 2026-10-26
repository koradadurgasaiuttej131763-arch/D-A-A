import time

n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

start = time.perf_counter()

for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

end = time.perf_counter()

print("Sorted array:", arr)
print("Execution Time:", end - start, "seconds")
print("Time Complexity:")
print("Best Case: O(n)")
print("Average Case: O(n²)")
print("Worst Case: O(n²)")
print("Space Complexity: O(1)")

# Logic

# * Assume the first element is already sorted.
# * Take the next element.
# * Insert it into the correct position in the sorted part.
# * Repeat for all remaining elements.