def solution(phone_book):
    s = set()
    
    for p in sorted(phone_book, key=lambda x : len(x)):
        for i in range(1, len(p) + 1):
            if p[:i] in s:
                return False
        s.add(p)
    return True