class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        Arrays.sort(trips, Comparator.<int[]>comparingInt(a -> a[1]));
        int current = 0;

        Queue<int[]> pq = new PriorityQueue<>(Comparator.<int[]>comparingInt(a -> a[0]));

        for (int[] trip : trips) {
            while (!pq.isEmpty() && pq.peek()[0] <= trip[1]) {
                int[] node = pq.poll();
                int count = node[1];
                current -= count;
            }

            if (current > capacity - trip[0]) {
                return false;
            }

            pq.add(new int[]{trip[2], trip[0]});
            current += trip[0];
        }
        return true;
    }
}