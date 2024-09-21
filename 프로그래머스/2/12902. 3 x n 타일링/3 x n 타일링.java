class Solution {
    public int solution(int n) {
        n /= 2;
        int d = 1_000_000_007;
        
        int[] dp = new int[n + 1];
        dp[1] = 3;
        dp[2] = dp[1]*3 + 2;
        int s = dp[1];
        
        for (int i=3; i<n+1; i++) {
            dp[i] += 2;
            dp[i] %= d;
            dp[i] += dp[i-1];
            dp[i] %= d;
            dp[i] += dp[i-1];
            dp[i] %= d;
            dp[i] += dp[i-1];
            dp[i] %= d;
            dp[i] += s;
            dp[i] %= d;
            dp[i] += s;
            dp[i] %= d;
            s += dp[i-1];
            s %= d;
        }
        
        return dp[n];
    }
}