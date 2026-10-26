import time

n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

start = time.perf_counter()

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

end = time.perf_counter()

print("Sorted array:", arr)
print("Execution Time:", end - start, "seconds")
print("Time Complexity:")
print("Best Case: O(n)")
print("Average Case: O(n²)")
print("Worst Case: O(n²)")

# Logic


# * Compare adjacent elements.
# * If the left element is greater than the right, swap them.
# * Repeat this process until no more swaps are needed.
# * After each pass, the largest element moves to the end like a bubble rising to the surface.
