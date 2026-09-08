class Solution {
    List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> combine(int n, int k) {
        dfs(n, k, 1, new ArrayList<>(k));
        return answer;
    }

    private void dfs(int n, int k, int start, List<Integer> current) {
        if (current.size() == k) {
            answer.add(new ArrayList<>(current));
            return;
        }

        int remaining = k - current.size();

        for (int i = start; i <= n - remaining + 1; i++) {
            current.add(i);
            dfs(n, k, i + 1, current);
            current.remove(current.size() - 1);
        }
    }
}