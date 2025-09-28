class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> counter = new HashMap<>();

        Queue<String> pq = new PriorityQueue<>(
                Comparator.<String>comparingInt(counter::get).reversed()
                    .thenComparing(Comparator.naturalOrder())
            );
        for (String w : words) {
            counter.merge(w, 1, (o,v) -> o + 1);
        }

        for (String word : counter.keySet()) {
            pq.add(word);
        }

        List<String> answer = new ArrayList<>(k);
        while (k-- > 0) {
            answer.add(pq.poll());
        }
        return answer;
    }
}