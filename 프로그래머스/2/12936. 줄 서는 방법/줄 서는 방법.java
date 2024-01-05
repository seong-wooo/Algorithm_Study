import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int n, long k) {
        List<Integer> nums = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            nums.add(i);
        }
        k--;
        
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            long fact = factorial(n - 1 - i);
            int nextIndex = (int) (k / fact);
            answer[i] = nums.remove(nextIndex);
            k %= fact;
        }
        
        return answer;
    }
    
    public long factorial(int n) {
        long result = 1;
        
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        
        return result;
    }
}