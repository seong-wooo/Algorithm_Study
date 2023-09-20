import sys

sys.stdin.readline()

n = sys.stdin.readline().split()

dict = {}

for x in n:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1


sys.stdin.readline()

m = sys.stdin.readline().split()

for i in m:
    if i in dict:
        print(dict[i], end=" ")
    else:
        print(0)
