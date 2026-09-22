class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) {
            return 0;
        }
        
        int left = 0;
        int current = 1;
        int count = 0;

        for (int right = 0; right < nums.length; right++) {
            current *= nums[right];

            while (current >= k) {
                current /= nums[left++];
            }
            count += right - left + 1;
            
        }
        return count;
    }
}