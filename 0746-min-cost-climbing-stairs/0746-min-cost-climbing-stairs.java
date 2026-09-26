class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        if (n == 2) {
            return Math.min(cost[0], cost[1]);
        }

        int[] dp = new int[n + 1];
        dp[1] = cost[0];
        dp[2] = cost[1];

        for (int i = 2; i < n; i++) {
            dp[i + 1] = (int) Math.min(dp[i], dp[i-1]) + cost[i];
        }

        return Math.min(dp[n], dp[n-1]);
    }
}