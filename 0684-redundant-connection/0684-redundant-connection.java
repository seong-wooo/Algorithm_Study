class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int[] parents = new int[edges.length + 1];
        for (int i = 0; i < parents.length; i++) {
            parents[i] = i;
        }

        List<int[]> answer = new ArrayList<>();

        for (int[] e : edges) {
            if (!union(parents, e[0], e[1])) {
                answer.add(e);
            }
        }

        return answer.get(answer.size() - 1);
    }

    private boolean union(int[] parents, int a, int b) {
        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
        }

        int pa = findParents(parents, a);
        int pb = findParents(parents, b);

        if (pa == pb) {
            return false;
        }
        parents[pb] = pa;
        return true;
    }

    private int findParents(int[] parents, int x) {
        if (parents[x] != x) {
            parents[x] = findParents(parents, parents[x]);
        }
        return parents[x];
    }
}