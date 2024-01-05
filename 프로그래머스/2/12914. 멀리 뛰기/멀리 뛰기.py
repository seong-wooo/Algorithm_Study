import sys

def solution(n):    
    sys.setrecursionlimit(10**6)
    return do(n, [1] * 2 + [0] * (n-1))
    
def do(n, dp):
    if dp[n] > 0:
        return dp[n]
    
    dp[n] = (do(n-1, dp) + do(n-2, dp)) % 1234567
    
    return dp[n] 