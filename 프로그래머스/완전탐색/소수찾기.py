#에라토네스의 체 이용 -> purmutation을 이용하여 각 개수별 소수를 구한다

from itertools import permutations

def solution(numbers):
    primes = [False, False] + [True] * 999999
    for i in range(2, int(1000001 ** 0.5) + 1):
        if primes[i]:
            primes[i * 2::i] = [False] * ((1000000 - i) // i)
    primes = set(x for x in range(1000000) if primes[x])

    prime_set = set()

    for x in range(1, len(numbers) + 1):
        combi = list(permutations(numbers, x))
        for i in combi:
            num = int("".join(i))
            print(num)
            if num in primes and num not in prime_set:
                prime_set.add(num)
    return len(prime_set)