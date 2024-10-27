import java.util.*;

class Solution {
    public int[] solution(int e, int[] starts) { 
        int[] factors = new int[e + 1];
        
        for (int i = 1; i < e + 1; i++) {
            for (int j = i; j < e + 1; j += i) {
                factors[j]++;
            }
        }
        
        int[] maxNum = new int[factors.length];
        
        int maxIndex = factors.length - 1;
        for (int i = factors.length - 1; i > 0; i--) {
            if (factors[i] >= factors[maxIndex]) {
                maxIndex = i;
            }
            maxNum[i] = maxIndex;
        }
        
        for (int i = 0; i < starts.length; i++) {
            starts[i] = maxNum[starts[i]];
        }
        return starts;
    }
}