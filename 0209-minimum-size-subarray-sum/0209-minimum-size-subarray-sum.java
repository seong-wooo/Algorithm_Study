class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0; 
        int current = 0;
        int answer = Integer.MAX_VALUE;

        for (int right = 0; right < nums.length; right++) {
            current += nums[right];

            while (left <= right && current >= target) {
                answer = (int) Math.min(answer, right - left + 1);
                current -= nums[left++];
            }
        }

        return answer == Integer.MAX_VALUE ? 0 : answer;
    }
}