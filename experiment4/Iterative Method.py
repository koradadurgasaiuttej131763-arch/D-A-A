import time

n = int(input("Enter a number: "))

start = time.perf_counter()

fact = 1

for i in range(1, n + 1):
    fact = fact * i

end = time.perf_counter()

print("Factorial of", n, "=", fact)
print("Execution Time:", end - start, "seconds")

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# 1. Take the number n.
# 2. Initialize fact = 1.
# 3. Run a loop from 1 to n.
# 4. Multiply fact by each number.
# 5. Print the final value.