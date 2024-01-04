import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Integer> pq = new PriorityQueue<>();
        Queue<int[]> q = new LinkedList<>();
        
        for (int i = 0; i < priorities.length; i++) {
            pq.add(-priorities[i]);
            q.add(new int[]{priorities[i], i});
        }
        
        int answer = 1;

        while(!q.isEmpty()) {
            if (q.peek()[0] == -pq.peek()) {
                int[] t = q.poll();
                if (t[1] == location) {
                    return answer;
                }
                pq.poll();
                answer++;
            } 
            else {
               q.add(q.poll()); 
            }
        }
        
        return answer;
    }
}