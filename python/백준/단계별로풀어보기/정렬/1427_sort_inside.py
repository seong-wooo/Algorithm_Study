# 문자열 -> 숫자 
# 숫자 -> 문자열 
# 바꾸는 방법만 알면 쉬운 문제

import sys

n = sys.stdin.readline().strip()
n = list(map(int, n))
n.sort(reverse=True)
print("".join(map(str, n)))