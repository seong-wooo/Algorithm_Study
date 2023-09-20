
# 나의 풀이 : brute force 방식 ( 시간 좀 걸림)
def solution(brown, yellow):
    # 가로, 세로를 a, b라고 하면
    # brown = a * 2 + b*2 -4
    # yellow = (a-2)*(b-2)

    for a in range(3, brown):
        for b in range(a, brown):
            if (brown, yellow) == (a * 2 + b * 2 - 4, (a - 2) * (b - 2)):
                return [b, a]

# 시간 엄청 조금 걸림
# 근의 공식을 이용 -> 변수 2개 식 2개이므로 근의 공식 사용 가능
import math
def solution(br,ye):
    w = 1+br/4 + math.sqrt((1+br/4)**2 -br-ye)
    h = 1+br/4 - math.sqrt((1+br/4)**2 -br-ye)
    return [w, h]