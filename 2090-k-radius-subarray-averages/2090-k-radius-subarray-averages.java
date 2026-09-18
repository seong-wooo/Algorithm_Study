class Solution {
    public int[] getAverages(int[] nums, int k) {
        int[] answer = new int[nums.length];
        Arrays.fill(answer, -1);

        if (nums.length < 2*k+ 1) {
            return answer;
        }

        long current = 0;
        for (int i = 0; i < 2*k + 1; i++) {
            current += nums[i];
        }

        answer[k] = (int) (current / (2 * k + 1));
        
        for (int i = k + 1; i < nums.length - k; i++) {
            current += nums[i + k] - nums[i - k - 1];
            answer[i] = (int) (current / (2 * k + 1));
        }
        return answer;
    }
}