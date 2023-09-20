def solution(n):
    m = [i for i in range(n)]
    result = 1
    for i in range(1,n//2+1):
        for j in range(i+1, n//2+2):
            s = sum(m[i:j+1])
            if n == s:
                result += 1
                break
            elif n <  s:
                break

    return result