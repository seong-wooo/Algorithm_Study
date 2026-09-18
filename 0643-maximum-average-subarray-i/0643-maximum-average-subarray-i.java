class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double total = 0;

        for (int i = 0; i < k; i++) {
            total += nums[i];
        }
        double answer = total / k;

        for (int i = k; i < nums.length; i++) {
            total += nums[i] - nums[i - k];
            answer = Math.max(answer, total / k);
        }

        return answer;
    }
}