class Solution {
    List<String> answer = new LinkedList<>();
    Map<String, Queue<String>> maps = new HashMap<>();

    public List<String> findItinerary(List<List<String>> tickets) {

        for (List<String> ticket : tickets) {
            maps.computeIfAbsent(ticket.get(0), k -> new PriorityQueue<>()).offer(ticket.get(1));
        }

        dfs("JFK");

        return answer;
    }

     private void dfs(String node) {

        Queue<String> pq = maps.get(node);

        while (pq != null && !pq.isEmpty()) {
            String next = pq.poll();
            dfs(next);
        }

        answer.add(0, node);
    }
}