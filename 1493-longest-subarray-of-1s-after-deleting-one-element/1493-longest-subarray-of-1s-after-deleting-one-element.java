class Solution {
    public int longestSubarray(int[] nums) {
        int left = 0;
        int zero = 0;

        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                zero++;
            }

            if (zero > 1) {
                if (nums[left++] == 0) {
                    zero--;
                }
            }
        }

        return nums.length - left - 1;
    }
}