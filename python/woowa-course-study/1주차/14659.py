input()

n = list(map(int, input().split()))
result = []
for i in range(len(n)):
    length = 0

    for j in range(i+1, len(n)):
        if n[i] < n[j]:
            length += j - i + 1
            break

        elif j == len(n):
            length += j - i

    result.append(length)



print(max(result))

