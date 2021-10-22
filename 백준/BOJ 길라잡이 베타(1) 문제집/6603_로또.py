# itertools의 combinations를 이용하여 풀었다.
# 총 nCk 개의 튜플을 리스트형식으로 반환

from itertools import combinations

while True:
    test = input()
    if test == "0":
        break

    k, *s = list(test.split())
    for i in combinations(s, 6):
        print(" ".join(i))
    print()


