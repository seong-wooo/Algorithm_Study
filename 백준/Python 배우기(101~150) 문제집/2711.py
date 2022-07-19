for i in range(int(input())):
    loc, message = input().split()
    print(message[:int(loc) - 1] + message[int(loc):])
