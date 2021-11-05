def solution(price, money, count):
    result = price * sum(range(1,count+1)) - money
    return result if result > 0 else 0