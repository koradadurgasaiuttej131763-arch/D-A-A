import time

n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

start = time.perf_counter()

found = False

for i in range(n):
    if arr[i] == key:
        found = True
        position = i
        break

end = time.perf_counter()

if found:
    print("Element found at index", position)
else:
    print("Element not found")

print("Execution Time:", end - start, "seconds")
print("Time Complexity:")
print("Best Case: O(1)")
print("Average Case: O(n)")
print("Worst Case: O(n)")
print("Space Complexity: O(1)")


# 1. Read all elements into an array.
# 2. Read the element to be searched.
# 3. Start from the first element.
# 4. Compare each element with the search key.
# 5. If a match is found, print its index and stop.
# 6. If the end of the array is reached without finding the key, print “Element not found.”