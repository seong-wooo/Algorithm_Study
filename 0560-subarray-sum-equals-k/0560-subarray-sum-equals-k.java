class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        counter.put(0, 1);
        int sum = 0, answer = 0;

        for (int num : nums) {
            sum += num;
            answer += counter.getOrDefault(sum - k, 0);
            counter.merge(sum, 1, Integer::sum);
        }
        return answer;
    }
}