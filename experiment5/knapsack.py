import time


def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

# Measure execution time
start_time = time.perf_counter()

max_value = knapsack(weights, values, capacity)

end_time = time.perf_counter()

execution_time = end_time - start_time

# Display results
print("Weights:", weights)
print("profits:", values)
print("max weight:", capacity)
print("Maximum profit:", max_value)
print("Execution Time:", execution_time, "seconds")

# Complexity
print("\nTime Complexity: O(n * W)")
print("Space Complexity: O(n * W)")

# What it does: Solves 0/1 Knapsack — take an item full or leave it, no breaking.
# Method: Dynamic Programming using a 2D table (dp).
# Table size: (n + 1) rows and (capacity + 1) columns, filled with 0s at start.
# Decision at each step:
# Fits: Choose the better option between take it or skip it.
# Doesn't fit: Just skip it (copy value from row above).
# Final answer: Stored in the bottom-right cell: dp[n][capacity].
# Time taken: $O(n \times W)$ (runs two simple loops).Memory used: $O(n \times W)$ (size of the 2D table).
# Bonus viva answer: We can reduce memory to $O(W)$ using a 1D array.