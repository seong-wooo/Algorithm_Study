class Solution {
    public int pivotIndex(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i-1];
        }

        for (int i = 0;  i < nums.length; i++) {
            int right = nums[nums.length - 1] - nums[i];
            int left = i == 0 ? 0 : nums[i - 1];
            if (left == right) {
                return i;
            }
        }
        return -1;
    }
}