import sys
from collections import Counter
input = sys.stdin.readline

while True:
    try:
        a, b = input().rstrip(), input().rstrip()

        c_a = Counter(a)
        c_b = Counter(b)
        result = Counter()

        for c in c_a.keys():
            if c in c_b:
                result[c] = min(c_a[c], c_b[c])

        print("".join(sorted(result.elements())))

    except:
        break

