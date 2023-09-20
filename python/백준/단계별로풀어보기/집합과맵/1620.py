import sys

n, m = map(int, sys.stdin.readline().split())
dict_num = {}
dict_pk = {}

ans = []
for i in range(1, int(n) + 1):
    pk = sys.stdin.readline().rstrip()
    dict_num[i] = pk
    dict_pk[pk] = i

for _ in range(m):
    pm = sys.stdin.readline().rstrip()
    if pm.isdigit():
        ans.append(dict_num[int(pm)])
    else:
        ans.append(str(dict_pk[pm]))

print("\n".join(ans))
