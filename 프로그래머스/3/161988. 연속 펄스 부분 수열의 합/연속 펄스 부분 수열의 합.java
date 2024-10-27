import java.util.*;

class Solution {
    public long solution(int[] sequence) {
        
        int[] pulse = new int[]{1,-1};
        int index = 0;
        long[][] dp = new long[2][sequence.length+1];
        long answer = sequence[0];
        
        for(int i = 1; i < dp[0].length; i++) {
            dp[0][i] = sequence[i-1] * pulse[index];
            if (dp[0][i-1] >= 0) {
                dp[0][i] += dp[0][i-1];
                answer = (long) Math.max(answer, dp[0][i]);
            }
            
            index++;
            index %= 2;
            
            dp[1][i] = sequence[i-1] * pulse[index];
            if (dp[1][i-1] >= 0) {
                dp[1][i] += dp[1][i-1];
                answer = (long) Math.max(answer, dp[1][i]);
            }
        }
        
        return answer;
    }
}