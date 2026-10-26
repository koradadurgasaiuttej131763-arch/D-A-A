import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

start = time.perf_counter()

sorted_arr = quicksort(arr)

end = time.perf_counter()

print("Sorted array:", sorted_arr)
print("Execution Time:", end - start, "seconds")
print("Time Complexity:")
print("Best Case: O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case: O(n²)")

# Logic

# * Choose one element as the pivot.
# * Place all smaller elements to the left of the pivot.
# * Place all larger elements to the right.
# * Repeat the same process on the left and right parts.