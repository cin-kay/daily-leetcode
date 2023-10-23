"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.



Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
"""


def is_power_of_four(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    n = 17
    print(is_power_of_four(n))
