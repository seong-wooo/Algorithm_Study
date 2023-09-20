import sys

n = int(sys.stdin.readline())
# k개 로프 중량 w -> 각 로프에 w/k 만큼 중량이 걸림
# w =  k * min ( rope k개 )

rope = [int(sys.stdin.readline()) for _ in range(n)]
rope.sort(reverse=True)
print(max((k+1) * r for k, r in enumerate(rope)))

