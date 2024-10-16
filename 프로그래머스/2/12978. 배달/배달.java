import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        Map<Integer, List<int[]>> path = new HashMap<>();
        Queue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        
        for (int[] r : road) {
            if (r[2] <= K) {
                if (!path.containsKey(r[0])) {
                    List<int[]> route = new ArrayList<>();
                    path.put(r[0], route);
                }
                path.get(r[0]).add(new int[]{r[1], r[2]});
                
                if (!path.containsKey(r[1])) {
                    List<int[]> route = new ArrayList<>();
                    path.put(r[1], route);
                }
                path.get(r[1]).add(new int[]{r[0], r[2]});
            }
        }
        
        int[] distance = new int[N + 1];
        int invalidDistance = K+1;
        Arrays.fill(distance, invalidDistance);
    
        pq.add(new int[]{1, 0});
        distance[1] = 0;
        
        while (!pq.isEmpty()) {
            int[] node_dist = pq.poll();
            int node = node_dist[0];
            int dist = node_dist[1];
            
            for (int[] next : path.get(node)) {
                int next_node = next[0];
                int next_distance = next[1] + dist;
                
                if (next_distance < distance[next_node]) {
                    distance[next_node] = next_distance;
                    pq.add(new int[]{next_node, next_distance});                 
                }
            }
        }
        
        int answer = 0;
        for (int i = 1; i <= N; i++) {
            if (distance[i] <= K) {
                answer++;
            }
        }
        return answer;
    }
}