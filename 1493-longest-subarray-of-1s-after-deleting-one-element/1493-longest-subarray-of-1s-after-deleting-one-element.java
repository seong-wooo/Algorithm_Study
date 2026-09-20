class Solution {
    public int longestSubarray(int[] nums) {
        int left = 0;
        int zero = -1;
        int answer = 0;


        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                if (zero >= 0) {
                    left = zero + 1;
                }
                zero = right;
            }
            answer = Math.max(answer, right - left + 1);
        }
        
        return answer - 1;
    }
}