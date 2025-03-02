# Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/?envType=daily-question&envId=2025-03-02
# Time: O(n + m)
# Space: O(n + m)


def merge_arrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    """
    Apply two pointers
    Input:
    nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
    ---
    Output: [[1,6],[2,3],[3,2],[4,6]]
    """
    n1 = len(nums1)
    n2 = len(nums2)

    res = []
    i1 = 0
    i2 = 0
    while i1 < n1 and i2 < n2:
        idx_1, val_1 = nums1[i1]
        idx_2, val_2 = nums2[i2]

        if idx_1 < idx_2:
            res.append([idx_1, val_1])
            i1 += 1
        elif idx_1 > idx_2:
            res.append([idx_2, val_2])
            i2 += 1
        else:
            res.append([idx_1, val_1 + val_2])
            i1 += 1
            i2 += 1

    while i1 < n1:
        res.append(nums1[i1])
        i1 += 1
    while i2 < n2:
        res.append(nums2[i2])
        i2 += 1

    return res


nums1 = [[1, 2], [2, 3], [4, 5]]
nums2 = [[1, 4], [3, 2], [4, 1]]
print(merge_arrays(nums1, nums2))
