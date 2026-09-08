class Solution {
    List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        dfs(nums, 0, new ArrayList<>());
        return answer;
    }

    private void dfs(int[] nums, int start, List<Integer> current) {
        if (start == nums.length) {
            answer.add(new ArrayList<>(current));
            return;
        }

        dfs(nums, start + 1, current);
        current.add(nums[start]);
        dfs(nums, start + 1, current);
        current.remove(current.size() - 1);
        
    }
}