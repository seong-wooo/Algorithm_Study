import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> q = new LinkedList<>();
        Queue<Integer> pq = new PriorityQueue<>((a, b) -> b-a);
        
        for (int i = 0; i < priorities.length; i++) {
            q.add(new int[]{priorities[i], i});
            pq.add(priorities[i]);
        }
        
        int answer = 1;
        while(!q.isEmpty()) {

            if (q.peek()[0] == pq.peek()) {
                pq.poll();
                int[] qp = q.poll();
                if (qp[1] == location) {
                    return answer;
                }
                answer++;
            } else {
                q.add(q.poll());    
            }
            
        }
        return -1;
    }
}