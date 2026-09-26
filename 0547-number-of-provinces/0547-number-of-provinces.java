class Solution {
    public int findCircleNum(int[][] isConnected) {
        int[] parents = new int[isConnected.length];
        for(int i = 0; i < parents.length; i++) {
            parents[i] = i;
        }

        for(int y = 0; y < isConnected.length; y++) {
            for(int x = 0; x < y; x++) {
                if (isConnected[y][x] == 1) {
                    union(parents, y, x);
                }
            }
        }

        Set<Integer> dup = new HashSet<>();
        for(int i = 0; i < parents.length; i++) {
            dup.add(findParent(parents, i));
        }

        return dup.size();
    }

    private void union(int[] parents, int a, int b) {
        int pa = findParent(parents, a);
        int pb = findParent(parents, b);

        if (pa > pb) {
            parents[pa] = pb;
        } else {
            parents[pb] = pa;
        }
    }

    private int findParent(int[] parents, int x) {
        if(parents[x] != x) {
            parents[x] = findParent(parents, parents[x]);
        }
        return parents[x];
    }
}