# Link: https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
# Time: O(n)
# Space: O(1)

# brute force
# get all sub array, calculate abs sum and return the max


def bf_max_abs_sum(nums: list[int]) -> int:
    n = len(nums)
    max_sum = 0
    for i in range(n):
        for j in range(i, n):
            sub_sum = abs(sum(nums[i : j + 1]))
            if max_sum < sub_sum:
                max_sum = sub_sum

    return max_sum


def max_abs_sum(nums: list[int]) -> int:
    # kadane's algo, but run for twice
    min_curr_sum = max_curr_sum = max_sum = min_sum = nums[0]
    for num in nums[1:]:
        max_curr_sum = max(max_curr_sum + num, num)
        max_sum = max(max_sum, max_curr_sum)

        min_curr_sum = min(min_curr_sum + num, num)
        min_sum = min(min_sum, min_curr_sum)

    return max(abs(max_sum), abs(min_sum))


nums = [1, -3, 2, 3, -4]
print(bf_max_abs_sum(nums) == max_abs_sum(nums))
