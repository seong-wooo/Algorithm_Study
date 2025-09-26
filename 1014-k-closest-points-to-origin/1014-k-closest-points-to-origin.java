class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Queue<int[]> pq = new PriorityQueue<>(
            (a, b) -> a[0]*a[0] + a[1]*a[1] - b[0]*b[0] - b[1]*b[1]
        );
        for (int[] p : points) {
            pq.add(p);
        }
        List<int[]> answer = new ArrayList<>();
        while (k-- > 0) {
            answer.add(pq.poll());
        }

        return answer.toArray(new int[answer.size()][]);
    }
}