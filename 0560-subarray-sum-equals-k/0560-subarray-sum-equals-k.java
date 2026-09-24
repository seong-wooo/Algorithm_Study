class Solution {
    public int subarraySum(int[] nums, int k) {
        int[] sum = new int[nums.length + 1];
        Map<Integer, Integer> counter = new HashMap<>();


        for (int i = 0; i < nums.length; i++) {
            sum[i+1] += sum[i] + nums[i];
        }

        int answer = 0;

        for(int i = 0; i < sum.length; i++) {
            answer += counter.getOrDefault(sum[i] - k, 0);
            counter.merge(sum[i], 1, Integer::sum);
        }

        return answer;
    }
}