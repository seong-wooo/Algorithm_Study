for _ in range(int(input())):
    n = int(input())
    sub_list = []
    print(f"Pairs for {n}: ",end = "")
    for i in range(1, n//2+1):
        if n - i != i:
            sub_list.append((i,n-i))
    for x in range(len(sub_list)-1):
        print(f"{sub_list[x][0]} {sub_list[x][1]}, ", end = "")
    if n > 2:
        print(sub_list[-1][0], sub_list[-1][1])
    else:
        print()