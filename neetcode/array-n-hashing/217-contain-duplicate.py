# Link: https://leetcode.com/problems/contains-duplicate/description/
# Time: O(n)
# Space: O(n)


def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


nums = [1, 2, 3, 1]
print(containsDuplicate(nums))  # True
