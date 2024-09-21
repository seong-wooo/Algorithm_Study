def solution(n):
    n //= 2
    dp = [0 for _ in range(n + 1)]
    dp[1] = 3
    dp[2] = 11
    
    s = dp[1]
    
    for i in range(3, n + 1):
        dp[i] += 2 + dp[i-1]*3 + s*2
        dp[i] %= 1000000007
        s += dp[i-1]
        s %= 1000000007
    
    return dp[n]