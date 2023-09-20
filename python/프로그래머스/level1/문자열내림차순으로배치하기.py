def solution(s):
    s = list(s)
    s.sort()
    return "".join(reversed(s))