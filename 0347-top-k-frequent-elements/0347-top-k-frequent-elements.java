class Solution {
    public int[] topKFrequent(int[] nums, int k) {
    
        Map<Integer, Integer> counter = new HashMap<>();

        Queue<Integer> pq = new PriorityQueue<>((a, b) -> counter.get(a) - counter.get(b));
        int[] answer = new int[k];

        for (int n : nums) {
            counter.merge(n, 1, Integer::sum);
        }

        for (int n : counter.keySet()) {
            if (pq.size() < k) {
                pq.add(n);
            } else if (counter.get(pq.peek()) < counter.get(n)) {
                pq.poll();
                pq.add(n);
            }
        }

        for (int i = 0; i < k; i++) {
            answer[i] = pq.poll();
        }

        return answer;
    }
}