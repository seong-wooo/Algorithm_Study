class Solution {
    private List<List<Integer>> answer = new ArrayList<>();


    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        dfs(candidates, target, 0, 0, new ArrayList<>());
        return answer;
    }

    private void dfs(int[] candidates, int target, int sum, int start, List<Integer> current) {
        if (target == sum) {
            answer.add(new ArrayList<>(current));
            return;
        }

        if (target < sum) {
            return;
        }

        for(int i = start; i < candidates.length; i++) {
            current.add(candidates[i]);
            dfs(candidates, target, sum + candidates[i], i, current);
            current.remove(current.size() - 1);
        }
    }
}