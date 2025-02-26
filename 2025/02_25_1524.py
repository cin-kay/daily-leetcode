# Link: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# Time: O(n)
# Space: O(1)
# Difficulty: Medium

"""
Explanation:
Use prefix sum to count number of odd sum of sub-array
Odd sum sub-array can be count if and only if
sum(sub-arr[i : j]) = prefix(j) - prefix(i - 1) is odd if prefix(j) and prefix(i - 1) has different parity
"""


def num_of_odd_sub_array(arr: list[int]) -> int:
    curr_sum = 0
    res = 0
    odd_count = 0
    event_count = 1

    for num in arr:
        curr_sum += num
        if curr_sum % 2 == 0:
            res += odd_count
            event_count += 1
        else:
            res += event_count
            odd_count += 1

    return res % (10**9 + 7)


arr = [1, 2, 3, 4]
print(num_of_odd_sub_array(arr))
