import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        int[] answer = new int[y + 1];
        int inf = 1000000;
        Arrays.fill(answer, inf);
        
        answer[x] = 0;
        
        for (int k = x; k < y + 1; k++) {
            if (k > n && answer[k - n] != inf) {
                answer[k] = answer[k - n] + 1;
            }
            if ((k / 2.0) % 1 == 0 && answer[k / 2] != inf) {
                answer[k] = (int) Math.min(answer[k], answer[k /2] + 1);
            }
            if ((k / 3.0) % 1 == 0 && answer[k / 3] != inf) {
                answer[k] = (int) Math.min(answer[k], answer[k /3] + 1);
            }
        }
        
        return answer[y] == inf ? -1 : answer[y];
    }
}