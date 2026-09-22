class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        return most(nums, k) - most(nums, k-1);
    }

    private int most(int[] nums, int k) {
        if (k < 0) {
            return 0;
        }
        int left = 0, count = 0, answer = 0;

        for (int right = 0; right < nums.length; right++) {
            count += nums[right] % 2 == 1 ? 1 : 0;

            while (count > k) {
                count -= nums[left++] % 2 == 1 ? 1 : 0;
            }

            answer += right - left + 1;
        }
        return answer;
    }
}