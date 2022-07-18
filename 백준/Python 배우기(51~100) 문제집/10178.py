for i in range(int(input())):
    candy, bro = map(int, input().split())
    print(f"You get {candy // bro} piece(s) and your dad gets {candy % bro} piece(s).")