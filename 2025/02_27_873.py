# Link: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/?envType=daily-question&envId=2025-02-27
# Time: O(n^2)
# Space: O(n)
# I made this thanks to ChatGPT :)

from collections import defaultdict


def longest_fib_sub_seq(arr: list[int]) -> int:
    if len(arr) < 3:
        return 0

    index = {x: i for i, x in enumerate(arr)}
    dp = defaultdict(lambda: 2)
    max_len = 0

    for j in range(len(arr)):
        for i in range(j):
            x = arr[j] - arr[i]
            if x in index and index[x] < i:
                k = index[x]
                dp[i, j] = dp[k, i] + 1
                max_len = max(max_len, dp[i, j])

    return max_len if max_len >= 3 else 0


# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(longest_fib_sub_seq(arr))  # 5
