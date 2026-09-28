class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Queue<int[]> pq = new PriorityQueue<>((a, b) -> a[0]*a[0] + a[1]*a[1] - b[0]*b[0] - b[1]*b[1]);

        for(int[] p : points) {
            pq.offer(p);
        }

        int[][] answer = new int[k][2];

        while(k > 0) {
            answer[answer.length - k] = pq.poll();
            k--;
        }

        return answer;

    }
}