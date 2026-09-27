class Solution {
    public int rob(int[] nums) {
        if (nums.length <= 2) {
            int max = 0;
            for(int n : nums) {
                max = Math.max(n, max);
            }
            return max;
        }
        
        int[] dp = new int[nums.length + 1];
        dp[1] = nums[0];
        dp[2] = nums[1];
        
        for (int i = 2; i < nums.length; i++) {
            dp[i+1] = Math.max(dp[i-1], dp[i-2]) + nums[i];
        }

        return Math.max(dp[dp.length -1], dp[dp.length -2]);
    }
}