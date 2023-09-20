from itertools import combinations


def solution(nums):
    primes = [False, False] + [True] * 2999

    for x in range(2, int(3000 ** 0.5) + 1):
        if x:
            primes[x + x::x] = [False] * ((3000 - x) // x)
    primes = set(x for x in range(2, 3001) if primes[x])

    three_nums = list(combinations(nums, 3))

    result = 0
    for i in three_nums:
        if sum(i) in primes:
            result += 1
    return result