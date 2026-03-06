# DP example — 0/1 Knapsack
# Practice: https://leetcode.com/problems/partition-equal-subset-sum/
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print("Max value =", knapsack(weights, values, capacity))
