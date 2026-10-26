import time

n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

start = time.perf_counter()

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

end = time.perf_counter()

print("Sorted array:", arr)
print("Execution Time:", end - start, "seconds")
print("Time Complexity:")
print("Best Case: O(n²)")
print("Average Case: O(n²)")
print("Worst Case: O(n²)")
print("Space Complexity: O(1)")

# Logic

# * Find the smallest element in the unsorted part of the array.
# * Swap it with the first unsorted position.
# * Repeat until the array is sorted.