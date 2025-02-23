# Link: https://neetcode.io/problems/string-encode-and-decode
# Time: O(n)
# Space: O(n)


def encode(strs: list[str]) -> str:
    """Encodes a list of strings into a single string."""
    return "".join(f"{len(s)}#{s}" for s in strs)


def decode(s: str) -> list[str]:
    """Decodes a single encoded string back into a list of strings."""
    res, i = [], 0
    while i < len(s):
        j = s.find("#", i)  # find next delimiter
        length = int(s[i:j])  # get the length of the string
        i = j + 1  # move past the delimiter
        res.append(s[i : i + length])  # get the actual string
        i += length  # move to the next encoded segment
    return res


# Example usage:
strings = ["apple", "banana", "kiwi"]
encoded = encode(strings)
decoded = decode(encoded)

print("Encoded:", repr(encoded))  # "5#apple6#banana4#kiwi"
print("Decoded:", decoded)  # ["apple", "banana", "kiwi"]
