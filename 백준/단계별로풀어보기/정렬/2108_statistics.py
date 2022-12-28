# 최빈값의 두 번째로 작은 값을 출력하는 것에서 어려움을 겪었다
# 최빈값을 찾아내고 그 중 두 번재로 작은 값을 찾아낼 때
# 리스트를 사용하여 접근시간을 줄였다.

import sys

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))


print(round(sum(num_list) / n))
print(sorted(num_list)[n//2])

b = [0] *8001
# 0 = 0 / -1 ~ -4000 =. 1~4000 / 1~ 4000 = 4001 ~ 8000

for i in num_list:
    if i > 0:
        b[i + 4000] += 1
    else:
        b[4000 + i] += 1

# 제일 많이 등장한 횟수
big_count = max(b)
count = 1

if b.count(big_count) == 1:
    index = b.index(big_count)
    if index > 4000:
        print(index - 4000)
    else:
        print(index-4000)
else:
    for i in range(len(b)):
        if b[i] == big_count and count == 0:
            if i > 4000:
                print(i - 4000)
                break
            else:
                print(i-4000)
                break
        elif b[i] == big_count and count == 1:
            count -= 1

print(max(num_list) - min(num_list))


# 최빈값을 구할때 Counter 클래스를 사용하여 구해보기
# 실행했을 때 실행 시간의 큰 차이는 없지만 훨씬 간결한 코드로 작성할 수 있었다.


# from collections import Counter
#
# counter = Counter(num_list).most_common()
# max_count = counter[0][1]
# count = []
# for i in range(len(counter)):
#     if counter[i][1] == max_count:
#         count.append(counter[i])
# if len(count) == 1:
#     print(count[0][0])
# else:
#     count.sort(key=lambda x:x[0])
#     print(count[1][0])