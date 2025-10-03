class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            if (k == 0) {
                break;
            }

            if (nums[i] < 0) {
                nums[i] = -nums[i];
                k--;
            }
        }

        return sum(nums, k % 2);
    }

    public int sum(int[] nums, int k) {
        int min = Integer.MAX_VALUE;
        int result = 0;
        for (int num : nums) {
            min = (int) Math.min(min, num);
            result += num;
        }

        if (k == 1) {
            return result - 2*min;
        }

        return result;
    }
}