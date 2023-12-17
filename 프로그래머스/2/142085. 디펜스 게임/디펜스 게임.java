import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        Queue<Integer> pq = new PriorityQueue<>();
        
        for(int i = 0; i < enemy.length; i++) {
            if (k > 0) {
                pq.add(enemy[i]);
                k--;
                continue;
            }
            
            if (n < pq.peek() && n < enemy[i]) {
                return i;
            }
            
            if (pq.peek() < enemy[i]) {
                n -= pq.poll();
                pq.add(enemy[i]);
            } else {
                n -= enemy[i];
            }
        
        }
        return enemy.length;
        
    }
}