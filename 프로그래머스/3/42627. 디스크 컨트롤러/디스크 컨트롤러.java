import java.util.*;
import java.util.stream.*;


class Solution {
    public int solution(int[][] js) {
        Arrays.sort(js, Comparator.comparing((int[] job) -> job[0]).thenComparing(job -> job[1]));
        
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparing((int[] job) -> job[1]).thenComparing(job -> job[0]));
        pq.add(js[0]);
        int index = 1;
        int currentTime = js[0][0];
        int answer = 0;
        
        while (!pq.isEmpty()) {
            int[] job = pq.poll();
           
            
            currentTime += job[1];
            answer += currentTime - job[0];
 
            while (index < js.length && js[index][0] <= currentTime) {
                pq.add(js[index]);
                index++;
            }
            
            if (pq.isEmpty() && index < js.length) {
                pq.add(js[index]);
                currentTime = js[index][0];
                index++;
            }
        }
        
        return answer / js.length;
    }
}