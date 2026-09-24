class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();

        for (int num : nums) {
            counter.merge(num, 1, Integer::sum);
        }

        Queue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(Map.Entry.comparingByValue());

        for (Map.Entry<Integer,Integer> entry : counter.entrySet()) {
            pq.offer(entry);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        int[] answer = new int[k];
        for (int i = 0; i < k; i++) {
            answer[i] = pq.poll().getKey();
        }
        return answer;
    }
}