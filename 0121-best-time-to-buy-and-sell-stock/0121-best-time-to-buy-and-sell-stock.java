class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int current = prices[0];

        for (int p : prices) {
            if (p > current) {
                max = Math.max(p - current, max);
            } else { 
                current = p;
            }
        }
        return max;
    }
}