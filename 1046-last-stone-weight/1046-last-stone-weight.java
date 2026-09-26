class Solution {
    public int lastStoneWeight(int[] stones) {
        Queue<Integer> pq = new PriorityQueue<>((a,b) -> b - a);

        for(int s : stones) {
            pq.offer(s);
        }

        while(pq.size() >= 2) { 
            int y = pq.poll();
            int x = pq.poll();

            if (y - x > 0) {
                pq.offer(y - x);
            }
        }

        return pq.isEmpty() ? 0 : pq.poll();
    }
}