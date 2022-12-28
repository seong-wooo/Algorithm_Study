# 처음 문자열을 받았을 때
# - 기호를 기준으로 split() 한다면
# 두 번째 요소부터는 - 기호 뒤에 있는 식들이다
# 따라서 각 요소를 괄호로 묶고 계산한다면 최솟값을 구할 수 있다.

import sys

s = sys.stdin.readline().strip()

divide_s = s.split("-")
total = sum(map(int, divide_s[0].split("+")))
for i in range(1, len(divide_s)):
    total -= sum(map(int,divide_s[i].split("+")))
print(total)
