class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double total = 0;

        for (int i = 0; i < k; i++) {
            total += nums[i];
        }
        double answer = total;

        for (int i = k; i < nums.length; i++) {
            total += nums[i] - nums[i - k];
            if (total > answer) {
                answer = total;
            }
        }

        return answer / k;
    }
}