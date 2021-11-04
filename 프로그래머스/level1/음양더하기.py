def solution(absolutes, signs):
    result = 0
    for i, j in zip(absolutes, signs):
        if j:
            result += i
        else:
            result -= i
    return result


# 이건 한줄로 구현
def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))