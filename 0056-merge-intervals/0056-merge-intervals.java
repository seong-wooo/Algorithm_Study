class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> answer = new ArrayList<>();
        Queue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        for(int[] itv : intervals) {
            pq.add(itv);
        }

        int[] current = pq.poll();

        while(!pq.isEmpty()) {
            int[] node = pq.poll();

            if (current[1] >= node[0]) {
                current[1] = (int) Math.max(current[1], node[1]);
                continue;
            } else {
                answer.add(current);
                current = node;
            }
        }

        answer.add(current);

        return answer.toArray(int[][]::new);
    }
}