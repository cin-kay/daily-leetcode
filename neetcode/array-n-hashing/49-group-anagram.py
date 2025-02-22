# Link: https://leetcode.com/problems/group-anagrams/description/
# Time: O(n)
# Space: O(n)


def group_anagrams(strs: list[str]) -> list[list[str]]:
    res = dict()
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in res:
            res[sorted_word] = [word]
        else:
            res[sorted_word].append(word)

    return list(res.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
