while(True):
    x = int(input())
    if x == -1:
        break
    a = []
    for i in range(1, x//2+1):
        if x%i ==0:
            a.append(i)
            a.append(x//i)
    a = list(set(a))
    a.sort()
    if x == sum(a[:-1]):
        print(f"{x} = ",end = "")
        for i in a[:-2]:
            print(i, end = " + ")
        print(a[-2])
    else:
        print(f"{x} is NOT perfect.")