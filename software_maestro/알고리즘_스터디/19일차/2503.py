import sys

input = sys.stdin.readline

n = int(input())

targets = set(str(i) for i in range(123, 1000) if "0" not in str(i) and len(set(str(i))) == 3)
num_s_b = []

for _ in range(n):
    num, s, b = input().split()
    num_s_b.append([num, int(s), int(b)])



def count_strike(target, num):
    return sum(target[i] == num[i] for i in range(3))

def count_ball_and_strike(target, num):
    return len(set(target) & set(num))


for i in range(n):
    num, s, b = num_s_b[i]

    remove_targets = set()
    for target in targets:
        strike = count_strike(target, num)
        ball = count_ball_and_strike(target, num) - strike

        if strike != s or ball != b:
            remove_targets.add(target)

    targets -= remove_targets


print(len(targets))