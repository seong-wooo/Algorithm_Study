# 큐를 이용하여 구현했다.
# 매번 pop과 append를 진행해서 엄청나게 많은 시간이 걸린다.(3208ms)
from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n + 1)])

result = "<"
while len(queue) > 1:
    for _ in range(k - 1):
        queue.append(queue.popleft())

    result += str(queue.popleft()) + ", "

result += str(queue[0]) + ">"

print(result)


#새로 다시 푼 풀이  (92ms)
# 없애야 하는 부분만 pop하여 pop 연산을 최소화하였다.
n, k = map(int, input().split())

arr = [i for i in range(1,n+1)]

result = "<"
index = -1
while len(arr) > 1:
  l = len(arr)
  index = (index + k) % l
  result += str(arr.pop(index)) + ", "
  index -= 1

result += str(arr[0]) + ">"
print(result)
