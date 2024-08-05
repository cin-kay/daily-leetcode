# def kthDistinct(arr: list[str], k: int) -> str:
#     str_set = dict()
#     for i in range(len(arr)):
#         if arr[i] not in str_set:
#             str_set[arr[i]] = 1
#         else:
#             str_set[arr[i]] += 1

#     dis_arr = [key for key, value in str_set.items() if value == 1]
#     if len(dis_arr) >= k:
#         return dis_arr[k - 1]
#     return ""


# arr = ["d", "b", "c", "b", "c", "a"]
# print(kthDistinct(arr, 2))

from collections import Counter
from typing import List


def countWords(words1: List[str], words2: List[str]) -> int:
    words1_counter = Counter(words1)
    words2_counter = Counter(words2)

    return len(
        [k for k, v in words1_counter.items() if v == 1 and words2_counter[v] == 1]
    )


words1 = ["leetcode", "is", "amazing", "as", "is"]
words2 = ["amazing", "leetcode", "is"]
print(countWords(words1, words2))  # 2
