def solution(s, n):
    result = ""
    for alpha in s:
        if 65 <= ord(alpha) <= 90:
            if ord(alpha) + n > 90:
                result += chr(64+(ord(alpha) + n)%90)
            else:
                result += chr(ord(alpha) + n)
        elif 97<=ord(alpha) <= 122:
            if ord(alpha) + n > 122:
                result += chr(96 + (ord(alpha) + n) % 122)
            else:
                result += chr(ord(alpha) + n)
        else:
            result += alpha
    return result