def solution(a, b):

    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
    return ["FRI","SAT","SUN","MON","TUE","WED","THU"][(sum(month[:a-1]) + b - 1) % 7]
    
