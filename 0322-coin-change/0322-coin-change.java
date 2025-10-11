class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int coin : coins) {
            if (coin <= amount) {
                dp[coin] = 1;
            }
        }

        for(int i = 1; i < dp.length; i++) {
            for (int c : coins) {
                if (c <= amount && i >= c && dp[i-c] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[i-c] + 1);
                }
            }
        }

        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }
}