
def mapUD(s):
    if s.isupper():
        return s.lower()
    return s.upper()

print("".join((map(mapUD, list(input())))))


## swapcase라는 함수가 있음
print(input().swapcase())