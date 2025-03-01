# Link: https://leetcode.com/problems/apply-operations-to-an-array/description/?envType=daily-question&envId=2025-03-01
# Time: O(n)
# Space: O(1)


def apply_operation_to_array(nums: list[int]) -> list[int]:
    # n = len(nums)
    # for i in range(n - 1):
    #     if nums[i] == nums[i + 1]:
    #         nums[i] *= 2
    #         nums[i + 1] = 0

    # zero_count = 0
    # res = []
    # for num in nums:
    #     if num == 0:
    #         zero_count += 1
    #     else:
    #         res.append(num)
    # res.extend([0] * zero_count) if zero_count > 1 else res
    # return res

    n = len(nums)
    j = 0

    for i in range(n):
        if i + 1 < n and nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums


nums = [1, 2, 2, 1, 1, 0]
print(apply_operation_to_array(nums))
