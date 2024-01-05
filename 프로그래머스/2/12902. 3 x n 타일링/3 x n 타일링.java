class Solution {
    public int solution(int n) {
        int d = 1_000_000_007;
        n /= 2;
        int[] dp = new int[n + 1];
        dp[1] = 3;
        dp[2] = 11;
        
        int sum = dp[1];
        for (int i = 3; i < n + 1; i++) {
            dp[i] += 2 + dp[i-1] * 2;
            dp[i] %= d;
            dp[i] += dp[i-1];
            dp[i] %= d;
            dp[i] += sum;
            dp[i] %= d;
            dp[i] += sum;
            dp[i] %= d;
            sum += dp[i - 1];
            sum %= d;
        }
        
        return dp[n];
    }
}