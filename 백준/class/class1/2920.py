a = list(map(int, input().split()))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = list(reversed(ascending))


if a == ascending:
    print("ascending")
elif a == descending:
    print("descending")
else:
    print("mixed")