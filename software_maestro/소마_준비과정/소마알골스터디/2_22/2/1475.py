from collections import Counter
import math

c = Counter(input())
# math.ceil("6" + "9" / 2) or 나머지

maximum = 0

if "6" in c:
    maximum += c["6"]

if "9" in c:
    maximum += c["9"]

maximum = math.ceil(maximum / 2)

for i in range(10):
    if i != 6 and i != 9 and str(i) in c:
        maximum = max(maximum, c[str(i)])

print(maximum)

