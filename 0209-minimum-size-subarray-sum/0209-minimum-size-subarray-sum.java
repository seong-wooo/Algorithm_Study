class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int cur = 0;
        int answer = Integer.MAX_VALUE;

        for (int right = 0; right < nums.length; right++) {
            cur += nums[right];

            while (cur >= target) {
                answer = Math.min(answer, right - left + 1);
                cur -= nums[left++];                
            }
        }

        return answer == Integer.MAX_VALUE ? 0 : answer;
    }
}