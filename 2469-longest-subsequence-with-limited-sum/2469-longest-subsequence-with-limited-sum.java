class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
        Arrays.sort(nums);

        int[] 누적합 = new int[nums.length + 1];
        
        for (int i = 1; i < nums.length + 1; i++) {
            누적합[i] = 누적합[i-1] + nums[i-1];
        }
 

        for (int i = 0; i < queries.length; i++) {
            int target = queries[i];
            queries[i] = count(누적합, target);
        }

        return queries;
    }

    public int count(int[] 누적합, int target) {
        for (int j = 1; j < 누적합.length; j++) {
            if (누적합[j] > target) {
                return j - 1;
            }
        }

        return 누적합.length - 1;
    }
}