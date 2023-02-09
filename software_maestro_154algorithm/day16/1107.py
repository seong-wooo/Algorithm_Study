import sys
input = sys.stdin.readline

n = int(input().strip())
m = input()
wrong = set(input().split())

channels = [str(i) for i in range(1000001)]



def isWrong(channel):
    if channel < 0 or channel >= len(channels):
        return True

    for num in str(channel):
        if num in wrong:
            return True
    return False

left_channel = n
right_channel = n
select_channel = 100

count = 0
while count < abs(n - 100):
    if not isWrong(left_channel):
        select_channel = left_channel
        break
    else:
        left_channel -= 1

    if not isWrong(right_channel):
        select_channel = right_channel
        break
    else:
        right_channel += 1

    count += 1


print(min(abs(n - 100), len(str(select_channel)) + abs(select_channel - n)))
