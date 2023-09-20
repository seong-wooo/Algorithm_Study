import sys

result = []
for i in range(int(sys.stdin.readline())):
    input = [list(sys.stdin.readline().strip().split(" ")) for k in range(int(sys.stdin.readline()))]
    print(max(input, key=lambda x : int(x[0]))[1])
