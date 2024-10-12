import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int sc : scoville) {
            pq.add(sc);
        }
        
        int answer = 0;
        
        while (pq.peek() < K) {
            int first = pq.poll();
            if (pq.isEmpty()) {
                return -1;
            }            
            pq.add(first + pq.poll()*2);
            answer++;
        }
        return answer;   
    }
}