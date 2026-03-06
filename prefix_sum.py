# Prefix sum example
# Practice: https://leetcode.com/problems/range-sum-query-immutable/
arr = [2, 4, 5, 7, 10]
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)

# Sum of elements from i to j inclusive
i, j = 1, 3
print("Sum from index", i, "to", j, "=", prefix[j+1] - prefix[i])
