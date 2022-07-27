import sys

result = []
for i in range(int(sys.stdin.readline())):
    age, name = sys.stdin.readline().split()
    result.append((int(age), name))

result.sort(key=lambda x:x[0])

for age, name in result:
    print(age, name)