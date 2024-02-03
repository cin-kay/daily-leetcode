"""
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence,
nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array,
leaving the remaining elements in their original order.
Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
"""


def constrained_subset_sum(nums: list[int], k: int) -> int:
    curr_sum = nums[0]
    res = 0
    for i in range(len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        res = max(res, curr_sum)

    if res == 0:
        return max(nums)
    return res


if __name__ == "__main__":
    nums = [-1, -2, -3]
    k = 1
    print(constrained_subset_sum(nums, k))
