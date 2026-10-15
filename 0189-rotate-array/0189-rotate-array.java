class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        int[] left = new int[nums.length - k];
        int[] right = new int[k];
        
        for(int i = nums.length - k; i <= nums.length - 1; i++) {
            right[i - nums.length + k] = nums[i];
        }

        for (int i = 0; i < nums.length - k; i++) {
            left[i] = nums[i];
        }

        for(int i = 0; i < right.length; i++) {
            nums[i] = right[i];
        }

        for (int i = right.length; i < nums.length; i++) {
            nums[i] = left[i - right.length];
        }
    }
}