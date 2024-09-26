def solution(word):

    return sum((5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1 for i, n in enumerate(word))