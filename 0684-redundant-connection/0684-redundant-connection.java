class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int[] parents = new int[edges.length + 1];
        for (int i = 0; i < parents.length; i++) {
            parents[i] = i;
        }

        for (int[] e : edges) {
            if (!union(parents, e[0], e[1])) {
                return e;
            }
        }

        return null;
    }

    private boolean union(int[] parents, int a, int b) {
        int pa = findParents(parents, a);
        int pb = findParents(parents, b);

        if (pa == pb) {
            return false;
        }

        if (pa > pb) {
            int temp = pa;
            pa = pb;
            pb = temp;
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