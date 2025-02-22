# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Time: O(n)
# Space: O(n)


def top_k_freq(nums: list[int], k: int) -> list[int]:
    num_freq = dict()
    for num in nums:
        if num not in num_freq:
            num_freq[num] = 1
        else:
            num_freq[num] += 1

    return sorted(num_freq, key=lambda x: num_freq[x], reverse=True)[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_freq(nums, k))
