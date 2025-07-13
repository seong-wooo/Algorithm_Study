class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for(int[] flight : flights) {
            graph.computeIfAbsent(flight[0], key -> new ArrayList<>()).add(new int[]{flight[1], flight[2]});
        }

        Queue<int[]> q = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        int[] visited = new int[n];
        Arrays.fill(visited, Integer.MAX_VALUE);

        q.add(new int[]{src, 0, -1});

        while (!q.isEmpty()) {
            int[] node = q.poll();
            int current = node[0];
            int time = node[1];
            int count = node[2];
            visited[current] = count;

            if (current == dst) {
                return time;
            }

            int nextCount = count + 1;
            if (nextCount <= k) {
                for(int[] next : graph.getOrDefault(current, List.of())) {
                    int nextNode= next[0];
                    int nextTime = time + next[1];
                    if (visited[nextNode] > nextCount) {
                        q.add(new int[]{nextNode, nextTime, nextCount});
                    }
                }
            }
        }

        return -1;
    }
}