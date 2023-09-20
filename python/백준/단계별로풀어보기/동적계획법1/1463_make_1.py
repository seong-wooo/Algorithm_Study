import sys
x = int(sys.stdin.readline())

count = [0] * (x + 1)

for i in range(2, x+1):
    count[i] = 1 + count[i-1]
    if i % 3 == 0:
        count[i] = min(count[i], 1 + count[i//3])
    if i % 2 == 0:
        # 여기서 if를 사용하는 것이 굉장히 중요하다!!
        # else if 사용 시 6의 배수에 대해서는 3으로 나눴을 때만 고려하는 것이므로 if를 사용한다.
        # 모든 경우를 고려해야한다.
        count[i] = min(count[i], 1 + count[i // 2])

print(count[x])
