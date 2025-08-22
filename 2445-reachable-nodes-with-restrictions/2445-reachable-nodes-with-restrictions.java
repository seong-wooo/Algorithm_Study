class Solution {
    public int reachableNodes(int n, int[][] edges, int[] restricted) {
        Map<Integer, List<Integer>> m = new HashMap<>();
        Set<Integer> s = new HashSet<>();

        for (int r : restricted) {
            s.add(r);
        }

        for (int[] e : edges) {
            if (!s.contains(e[0])) {
                m.computeIfAbsent(e[0], k -> new ArrayList<>()).add(e[1]);
            }
            if (!s.contains(e[1])) {
                m.computeIfAbsent(e[1], k -> new ArrayList<>()).add(e[0]);
            }
        }

        Queue<Integer> q = new ArrayDeque<>();

        q.addAll(m.get(0));

        Set<Integer> visited = new HashSet<>();
        visited.add(0);

        while (!q.isEmpty()) {
            int next = q.poll();

            if (!s.contains(next) && !visited.contains(next)) {
                q.addAll(m.get(next));
                visited.add(next);
            }
        }

        return visited.size();
    }
}