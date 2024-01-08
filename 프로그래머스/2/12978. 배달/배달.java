import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        Map<Integer, List<int[]>> graph = new HashMap<>();
        Queue<int[]> q = new PriorityQueue<>((x, y) -> x[1] - y[1]);
        
        for (int[] abc : road) {
            if (abc[2] <= K) {
                List<int[]> route = new ArrayList<>();
                route.add(new int[]{abc[1], abc[2]});
                graph.merge(abc[0], route, (o, v) -> {
                    o.addAll(route);
                    return o;
                });
                
                List<int[]> route2 = new ArrayList<>();
                route2.add(new int[]{abc[0], abc[2]});
                graph.merge(abc[1], route2, (o, v) -> {
                    o.addAll(route2);
                    return o;
                });
            }
        }
        
        int invalidD = K + 1;
        int[] distance = new int[N + 1];
        Arrays.fill(distance, 2, N + 1, invalidD);
        int answer = 1;
        for (int[] bc : graph.get(1)) {
            if (bc[1] <= K) {
                q.add(bc);
            }
        }
        
        while (!q.isEmpty()) {
            int[] bc = q.poll();
            if (distance[bc[0]] == invalidD) {
                distance[bc[0]] = bc[1];
                for (int[] ac : graph.get(bc[0])) {
                    int nextDistance = bc[1] + ac[1];
                    if (distance[ac[0]] == invalidD && nextDistance <= K) {
                        q.add(new int[]{ac[0], nextDistance});
                    }
                }
                answer++;
            }
            
        }

        return answer;
        
    }
}