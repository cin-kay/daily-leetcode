# Link: https://leetcode.com/problems/valid-anagram/description/
# Time: O(n)
# Space: O(1)

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


s = "ccaac"
t = "aaccc"
print(is_anagram(s, t))
