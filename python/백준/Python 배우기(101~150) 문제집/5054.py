for i in range(int(input())):
    n = input()
    stores = list(sorted((map(int, input().split()))))
    print((stores[-1] - stores[0]) * 2)



