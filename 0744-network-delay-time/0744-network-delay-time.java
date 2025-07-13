class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        // u -> v w: 도착시간

        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int[] time: times) {
            graph.computeIfAbsent(time[0], key -> new ArrayList<>()).add(new int[]{time[1], time[2]});
        }

        int[] delay = new int[n+1];
        Arrays.fill(delay, Integer.MAX_VALUE);
        delay[0] = 0;
        
        Queue<int[]> q = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        q.add(new int[]{k, 0});
        
        while (!q.isEmpty()) {
            int[] node = q.poll();
            if (delay[node[0]] == Integer.MAX_VALUE) {
                delay[node[0]] = node[1];
                if (graph.containsKey(node[0])) {
                    for (int[] time : graph.get(node[0])) {
                        if (delay[time[0]] > time[1] + delay[node[0]]) {
                            q.add(new int[]{time[0], time[1] + delay[node[0]]});
                        }
                    }
                }
            }
        }

        int answer = 0;

        for (int d : delay) {
            if (d == Integer.MAX_VALUE) {
                return -1;
            }
            answer = (int) Math.max(answer, d);
        }
        return answer;
    }
}