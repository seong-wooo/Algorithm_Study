def solution(phone_book):
    s = set()
    phone_book.sort(key = lambda x : len(x))
    
    for p in phone_book:
        for i in range(1, len(p) + 1):
            if p[:i] in s:
                return False
        s.add(p)
    return True