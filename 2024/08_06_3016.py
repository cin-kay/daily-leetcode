from collections import Counter


def minimumPushes(word: str) -> int:
    word_set = Counter(word) 
    sorted_counts = dict(sorted(word_set.items(), key=lambda x: x[1], reverse=True))
    total_key_presses = 0
    for index, item in enumerate(sorted_counts.items()):
        if item[-1] == 0:
            break
        total_key_presses += (index // 8 + 1) * item[-1]

    return total_key_presses


word = "abcde"
print(minimumPushes(word))
