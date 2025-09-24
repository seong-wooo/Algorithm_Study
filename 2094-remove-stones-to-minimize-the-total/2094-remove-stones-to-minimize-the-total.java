class Solution {
    public int minStoneSum(int[] piles, int k) {
        Queue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);

        for (int p : piles) {
            pq.add(p);
        }

        while (k-- > 0) {
            int stone = pq.poll();
            pq.add(stone - (int) Math.floor(stone / 2));
        }

        int result = 0;
        for (int p : pq) {
            result += p;
        }
        return result;
    }
}