class Solution {
    public int minOperations(int[] nums, int x) {
        int total = 0;
        for (int n : nums) {
            total += n;
        }

        int left = 0;
        int current = 0;
        int answer = Integer.MAX_VALUE;

        for (int right = 0; right < nums.length; right++) {
            current += nums[right];

            while(current > total - x && left <= right) {
                current -= nums[left++];
            }

            if (current == total - x) {
                answer = Math.min(answer, left + nums.length - 1 - right);
            }
        }

        return answer == Integer.MAX_VALUE ? -1 : answer;
    }
}