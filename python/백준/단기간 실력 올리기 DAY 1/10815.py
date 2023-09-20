n = input()
sang = set(map(int, input().split()))

m = input()
for num in map(int, input().split()):
    if num in sang:
        print("1", end=" ")
    else:
        print("0", end=" ")
