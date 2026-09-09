class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<int[]>> nodeTime = new HashMap<>();
        
        for (int[] time : times) {
            nodeTime.computeIfAbsent(time[0], x -> new ArrayList<>()).add(new int[]{time[1], time[2]});
        }

        Queue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        int[] arrive = new int[n+1];
        Arrays.fill(arrive, Integer.MAX_VALUE);

        pq.add(new int[]{k, 0});
        arrive[k] = 0;
        
        while (!pq.isEmpty()) {
            int[] node = pq.poll();
            int num = node[0];
            int time = node[1];

            for (int[] nt : nodeTime.getOrDefault(num, List.of())) { 
                int nextNum = nt[0];
                int nextTime = nt[1];

                if (time + nextTime < arrive[nextNum]) {
                    arrive[nextNum] = time + nextTime;
                    pq.offer(new int[]{nextNum, arrive[nextNum]});
                }
            }
        }

        int result = Integer.MIN_VALUE;
        for (int i = 1; i < n+1;i++) {
            result = (int)Math.max(arrive[i], result);
        }
        return result == Integer.MAX_VALUE ? -1 : result;

    }
}