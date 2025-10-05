class Solution {
    public int totalNQueens(int n) {
        return dfs(n, new ArrayList<>(), new HashSet<>());
    }

    public int dfs(int n, List<Integer> prev, Set<Integer> column) {
        if (prev.size() == n) {
            return 1;
        }
        int result = 0;

        for (int i = 0; i < n; i++) {
            if (!column.contains(i) && !대각선_포함됐나(i, prev)) {
                prev.add(i);
                column.add(i);
                result += dfs(n, prev, column);
                prev.remove(prev.size() - 1);
                column.remove(i);
            }
        }
        return result;
    }

    public boolean 대각선_포함됐나(int index, List<Integer> prev) {
        int 높이 = prev.size();

        for (int i = 0; i < prev.size(); i++) {
            int 높이차이 = 높이 - i;
            if (prev.get(i) == index + 높이차이  || prev.get(i) == index - 높이차이) {
                return true;
            }
        }

        return false;
    }
}