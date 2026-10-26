import time

n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

arr.sort()

key = int(input("Enter element to search: "))

start = time.perf_counter()

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        found = True
        position = mid
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

end = time.perf_counter()

print("Sorted array:", arr)

if found:
    print("Element found at index", position)
else:
    print("Element not found")

print("Execution Time:", end - start, "seconds")
print("Time Complexity:")
print("Best Case: O(1)")
print("Average Case: O(log n)")
print("Worst Case: O(log n)")
print("Space Complexity: O(1)")

# 1. Ensure the array is sorted.
# 2. Set low = 0 and high = n - 1.
# 3. Find the middle element:
#     * mid = (low + high) // 2
# 4. Compare the middle element with the search key:
#     * If equal → Element found.
#     * If the key is greater → Search the right half (low = mid + 1).
#     * If the key is smaller → Search the left half (high = mid - 1).
# 5. Repeat until the element is found or low > high.