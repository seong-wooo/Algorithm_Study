for i in range(int(input())):
    n = list(reversed(str(bin(int(input())))))
    for j in range(len(n) - 2):
        if n[j] == "1":
            print(j, end=" ")
