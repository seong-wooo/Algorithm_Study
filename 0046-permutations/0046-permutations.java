class Solution {
    List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {
        dfs(nums, new HashSet<>(), new ArrayList<>());
        return answer;
    }

    private void dfs(int[] nums, Set<Integer> visited, List<Integer> current) {
        if (current.size() == nums.length) {
            answer.add(new ArrayList<>(current));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (visited.contains(i)) {
                continue;
            }
            visited.add(i);
            current.add(nums[i]);
            dfs(nums, visited, current);
            visited.remove(i);
            current.remove(current.size() - 1);
        }
    }
}