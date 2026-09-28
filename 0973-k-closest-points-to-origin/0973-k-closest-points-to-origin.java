class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Queue<int[]> pq = new PriorityQueue<>((a, b) -> b[0]*b[0] + b[1]*b[1] - a[0]*a[0] - a[1]*a[1]);

        for(int[] p : points) {
            pq.offer(p);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        int[][] answer = new int[k][2];

        while(k > 0) {
            answer[k - 1] = pq.poll();
            k--;
        }

        return answer;

    }
}