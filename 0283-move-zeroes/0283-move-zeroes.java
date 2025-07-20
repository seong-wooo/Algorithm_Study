class Solution {
    public void moveZeroes(int[] nums) {
        int left = 0;
        int right = 0;

        while (right < nums.length) {
            while (left < nums.length && nums[left] != 0) {
                left++;
            }

            right = left + 1;
            while (right < nums.length && nums[right] == 0) {
                right++;
            }

            if (right < nums.length) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
            }
        }
    }
}