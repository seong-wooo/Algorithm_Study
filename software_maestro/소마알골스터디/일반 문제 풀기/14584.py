import sys
input = sys.stdin.readline

secrets = input().rstrip()
d = set(input().rstrip() for _ in range(int(input())))


# a ~ z 97 ~ 122
def change(secrets, i):
    result = ""
    for s in secrets:
        if ord(s) + i  > 122:
            result += chr(ord(s) + i - 26)
        else:
            result += chr(ord(s) + i)
    return result


def find_secrets():
    for i in range(26):
        s = change(secrets, i)
        for word in d:
            if word in s:
                return s


print(find_secrets())