class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        int[] parent = new int[n];
        for (int i = 0; i < parent.length; i++) {
            parent[i] = i;
        }

        for (int[] e : edges) {
            union(e[0], e[1], parent);
        }

        return findParent(source,parent) == findParent(destination,parent);
    }

    public void union(int a, int b, int[] parent) {
        int fa = findParent(a, parent);
        int fb = findParent(b, parent);

        if (fa > fb) {
            parent[fa] = fb;
        } else {
            parent[fb] = fa;
        }
    } 

    public int findParent(int a, int[] parent) {
        if (parent[a] != a) {
            parent[a] = findParent(parent[a], parent);
        }
        return parent[a];
    }
}