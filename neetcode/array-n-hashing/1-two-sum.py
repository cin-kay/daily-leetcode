# Link: https://leetcode.com/problems/two-sum/description/
# Time: O(n)
# Space: O(n)


def two_sum(nums: list[int], target: int) -> list[int]:
    num_set = dict()
    for i, num in enumerate(nums):
        if num in num_set:
            return [num_set[num], i]
        num_set[target - num] = i

    return []


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # [0, 1]
