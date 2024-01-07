def solution(n, t, m, p):
    
    max_length = m * (t - 1) + p
    
    base = ""
    num = 0
    while len(base) < max_length:
        base += toN(num, n)
        num += 1
    
    return base[p-1::m][:t]


def toN(num, n):
    a = [str(i) for i in range(16)]
    a[10:16] = ["A", "B", "C", "D", "E", "F"]
    
    result = ""
    
    while num >= n:
        num, r = num // n, num % n
        result = a[r] + result
    return a[num] + result