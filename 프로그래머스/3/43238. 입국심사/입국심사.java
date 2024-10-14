import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long left = 1;
        long right = (long) Arrays.stream(times).min().getAsInt() * n;
        long answer = 0;
        
        while (left <= right) {
            long mid = left + (right - left) / 2;
            long target = 0;
            
            for (long time : times) {
                target += (mid / time);
            }
            
            if (target >= n) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid +1;
            }
            
        }
        
        return answer;
    }
}