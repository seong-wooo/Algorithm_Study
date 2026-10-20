class Solution {
    public int maxProduct(int[] nums) {
        int currentMax = nums[0];
        int currentMin = nums[0];
        int answer = nums[0];

        for(int i = 1; i < nums.length; i++) {
            int n = nums[i];
            int a = currentMax * n;
            int b = currentMin * n;

            currentMax = Math.max(n, Math.max(a, b));
            currentMin = Math.min(n, Math.min(a, b));

            answer = Math.max(currentMax, answer);
        }
        return answer;
    }
}