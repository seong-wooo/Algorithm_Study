class Solution {
    public int solution(int n) {
        int[] dp = new int[n + 1];
        dp[2] = 3;
        dp[4] = 11;
        
        for (int i = 6; i <= n; i += 2) {
            dp[i] = (2 + dp[i - 2] * 3) % 1000_000_007;
            for (int j = 4; j < i; j += 2) {
                dp[i] += (dp[i - j] * 2) % 1000_000_007;
                dp[i] %= 1000_000_007;
            }
        }
        
        return dp[n];
    }
}