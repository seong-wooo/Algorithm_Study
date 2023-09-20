import sys

input = sys.stdin.readline

n = int(input())

cards = [0] + list(map(int, input().split()))

for i in range(2, n + 1):
    for j in range(1, i):
        cards[i] = min(cards[i], cards[j] + cards[i - j])


print(cards[n])