class Solution {
    List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> combine(int n, int k) {
        dfs(n, k, new LinkedList<>());
        return answer;
    }

    private void dfs(int n, int k, Deque<Integer> current) {
        if (current.size() == k) {
            answer.add(new ArrayList<>(current));
            return;
        }


        for(int i = current.isEmpty() ? 1 : current.peekLast() + 1; i <= n; i++) {
            current.offer(i);
            dfs(n, k, current);
            current.removeLast();
        }
    }
}