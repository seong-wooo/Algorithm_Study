def solution(phone_book):
    phone = set()
    
    for p in sorted(phone_book, key = lambda x : len(x)):
        for i in range(1, len(p)):
            if p[:i] in phone:
                return False
        phone.add(p)
    return True