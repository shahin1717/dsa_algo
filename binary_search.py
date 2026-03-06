# Binary search template
# Practice: https://leetcode.com/problems/binary-search/
import bisect

arr = [1, 3, 5, 7, 9, 12, 15]
x = 7

# Manual binary search
lo, hi = 0, len(arr) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == x:
        print("Found at index", mid)
        break
    elif arr[mid] < x:
        lo = mid + 1
    else:
        hi = mid - 1

# Using bisect
idx = bisect.bisect_left(arr, x)
print("bisect result:", idx)
