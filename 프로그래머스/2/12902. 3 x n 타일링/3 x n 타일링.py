def solution(n):
    dp = [0] * (n + 1)
    dp[2] = 3
    dp[4] = 11
    
    for i in range(6, n + 1, 2):
        dp[i] = 2 + dp[i-2] * 3
        for j in range(4, i, 2):
            dp[i] += dp[i-j] * 2 
            dp[i] %= 1000_000_007
    return dp[n]