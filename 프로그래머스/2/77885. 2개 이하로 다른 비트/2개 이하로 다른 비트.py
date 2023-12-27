import sys

def solution(numbers):
    
    return list(map(lambda x : find(x), numbers))
    

def find(x):
    bx = bin(x)[2:]
    result = int("10" + bx[1:], 2)
    
    for i in range(len(bx)):
        if bx[i] == "0":
            result = min(result, int(bx[:i] + "1" + bx[i+1:], 2))
            if i != len(bx) - 1:
                result = min(result, int(bx[:i] + "10" + bx[i+2:], 2))
    return result