import java.util.*;

class Solution {
    public int solution(int n) {
        int[] before = new int[n];
        return queen(before, n, 0);
    }
    
    public int queen(int[] before, int n, int current) {
        if (current == n) {
            return 1;
        }
        
        boolean[] inValid = new boolean[n];
    
        for (int i = 0; i < current; i++) {
            inValid[before[i]] = true;
            int right = before[i] + current - i;
            int left = before[i] - current + i;
            
            if (right < n) {
                inValid[right] = true;
            }
            if (0 <= left) {
                inValid[left] = true;
            }
        }
        
        int answer = 0;
        
        for (int j = 0; j < n; j++) {
            if (!inValid[j]) {
                before[current] = j;
                answer += queen(before, n, current + 1);
                before[current] = 0;
            }
        }
        
        return answer;
    }
}