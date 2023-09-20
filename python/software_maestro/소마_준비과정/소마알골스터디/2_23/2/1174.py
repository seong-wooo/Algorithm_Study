from itertools import combinations

n = int(input())
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if n >= 1024:
    print(-1)

else:
    for i in range(1, 11):
        combi = list(combinations(nums, i))
        if n > len(combi):
            n -= len(combi)
        else:
            for i in range(len(combi)):
                combi[i] = "".join(map(str, reversed(combi[i])))
            combi.sort()
            print(combi[n - 1])
            n = 0
            break
