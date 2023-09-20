import sys

for t in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    first = list(map(int, sys.stdin.readline().split()))
    second = list(map(int, sys.stdin.readline().split()))

    dp1 = [first[0]]
    dp2 = [second[0]]

    for i in range(1, n):
        result1 = max(dp2[i-1] + first[i], dp1[i-1])
        result2 = max(dp1[i-1] + second[i], dp2[i-1])

        dp1.append(result1)
        dp2.append(result2)

    print(max(dp1[-1], dp2[-1]))
