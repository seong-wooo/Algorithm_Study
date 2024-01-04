import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] scoville, int K) {
        Queue<Integer> pq = new PriorityQueue<Integer>();
        int answer = 0;
        for (int s : scoville) {
            pq.add(s);
        }
        
        while (pq.peek() < K) {
            int s1 = pq.poll();
            if (pq.isEmpty()) {
                return -1;
            }
            int s2 = pq.poll();
            
            pq.add(s1 + s2*2);
            answer++;
        }
        
        return answer;
    }
}