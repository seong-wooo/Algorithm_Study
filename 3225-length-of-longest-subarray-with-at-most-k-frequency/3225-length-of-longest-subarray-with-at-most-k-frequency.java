class Solution {
    int answer = 0;

    public int maxSubarrayLength(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        int current = 0;
        int left = 0;

        for (int right = 0; right < nums.length; right++) {
            counter.merge(nums[right], 1, (o, v) -> o + 1);
            
            while (counter.get(nums[right]) > k && left <= right) {
                counter.merge(nums[left], 0, (o, v) -> o-1);
                left++;
            }
            answer = Math.max(right - left + 1, answer);
        }

        return answer;
    }
}