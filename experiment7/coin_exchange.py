import time

def coin_change(coins, amount):
    # dp[i] = minimum number of coins required to make amount i
    dp = [float('inf')] * (amount + 1)

    # Base case: 0 coins are needed to make amount 0
    dp[0] = 0

    # Calculate minimum coins for every amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If amount cannot be formed
    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


# Input
coins = [1, 2, 5, 10]
amount = int(input("enter the amount:"))

# Measure execution time
start_time = time.perf_counter()

result = coin_change(coins, amount)

end_time = time.perf_counter()

execution_time = end_time - start_time

# Output
print("Coins:", coins)
print("Amount:", amount)

if result == -1:
    print("The amount cannot be formed using the given coins.")
else:
    print("Minimum number of coins required:", result)

print("Execution time:", execution_time, "seconds")
print("Time Complexity: O(n × A)")
print("Space Complexity: O(A)")

# What it does: Solves the Coin Change Problem — finds the minimum number of coins 
# needed to make a target amount.Method: Dynamic Programming using a 1D array (dp).
# Table meaning: dp[i] is the fewest coins needed to make amount i.
# Initialization:
#   Filled with infinity (unreachable amounts).
#   dp[0] = 0 (zero coins needed to make amount 0).
# Formula at each step:
#   For each coin, if it fits: dp[i] = min(dp[i], dp[i - coin] + 1).
#   The + 1 represents using that current coin.
# Final check:
#   If dp[amount] is still infinity, return -1 (cannot make the exact amount).
#   Otherwise, return dp[amount].
# Time Complexity: $O(n \times A)$ — outer loop for amounts ($A$), inner loop for coins ($n$).
# Space Complexity: $O(A)$ — single array of size amount + 1.
# Viva Tip: Greedy algorithm fails for arbitrary coin systems, 
#           so Dynamic Programming is used to guarantee the optimal answer.