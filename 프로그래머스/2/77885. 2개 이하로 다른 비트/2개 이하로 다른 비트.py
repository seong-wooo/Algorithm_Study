def solution(numbers):
    return list(map(change, numbers))

def change(num):
    if num % 2 == 0:
        return num + 1
    
    b_num = "0" + bin(num)[2:]
    
    for i in range(len(b_num) - 2, -1, -1):
        if b_num[i:i+2] == "01":
            return int(b_num[:i] + "10" + b_num[i+2:], 2)