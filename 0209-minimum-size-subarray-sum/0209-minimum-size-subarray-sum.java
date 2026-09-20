class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int current = 0;

        int left = 0;
        int right = 0;

        int answer = Integer.MAX_VALUE;


        while (right < nums.length) {
            current += nums[right];
            while (target > current && right < nums.length - 1) {
                current += nums[++right];
            }

            while (left < right && current - nums[left] >= target) {
                current -= nums[left++];
            }

            if (current >= target) {
                answer = (int) Math.min(answer, right - left + 1);
            }

            right++;
        }

        return answer == Integer.MAX_VALUE ? 0 : answer;
    }
}