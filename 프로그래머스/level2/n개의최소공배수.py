#gcd 이용하여 간단하게 해결
from math import gcd
def solution(arr):
    for i in range(len(arr)-1):
        arr[i+1] = (arr[i] * arr[i+1]) // gcd(arr[i], arr[i+1])
    return arr[-1]