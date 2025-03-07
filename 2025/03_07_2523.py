# Link: https://leetcode.com/problems/closest-prime-numbers-in-range/
# Time: O(n * log(log(n)))
# Space: O(n)


def is_prime(num: int) -> bool:
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def closest_primes(left: int, right: int) -> list[int]:
    primes = [num for num in range(left, right + 1) if is_prime(num)]

    if len(primes) < 2:
        return [-1, -1]

    min_pair = [primes[0], primes[1]]
    min_diff = primes[1] - primes[0]

    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] < min_diff:
            min_pair = [primes[i], primes[i + 1]]
            min_diff = primes[i + 1] - primes[i]

    return min_pair


left, right = 10, 19
print(closest_primes(left, right))  # [11, 13]
