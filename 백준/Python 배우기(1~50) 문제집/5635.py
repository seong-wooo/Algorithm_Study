import sys

members = []
for i in range(int(sys.stdin.readline())):
    members.append(list(sys.stdin.readline().strip().split()))


sortedMembers = sorted(members, key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(f"{sortedMembers[-1][0]}\n{sortedMembers[0][0]}")
