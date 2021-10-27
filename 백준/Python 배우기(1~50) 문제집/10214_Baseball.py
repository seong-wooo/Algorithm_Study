y, k = 0 ,0
for _ in range(int(input())):
    for i in range(9):
        ye, ko = map(int,input().split())
        y += ye
        k += ko
    print("Yonsei" if y > k else "Korea" )