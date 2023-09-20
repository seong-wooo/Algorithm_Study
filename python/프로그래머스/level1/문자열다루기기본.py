#내가 푼 풀이
def solution(s):
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        return True
    return False

# 더 깔끔하게 푼 풀이
def solution(s):
    return s.isdigit() and len(s) in (4, 6)