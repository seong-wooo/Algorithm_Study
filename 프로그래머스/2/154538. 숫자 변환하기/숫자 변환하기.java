import java.util.*;

class Solution {
    
    public int solution(int x, int y, int n) {
        
        int[] counts = new int[y+1];
        Arrays.fill(counts, 1_000_001);
        counts[x] = 0;
        
        
        for (int i = x; i < counts.length; i++) {
            if (i % 2 == 0 && i / 2 >= x) {
                counts[i] = (int) Math.min(counts[i], counts[i/2] + 1);
            }
            
            if (i % 3 == 0 && i / 3 >= x) {
                counts[i] = (int) Math.min(counts[i], counts[i/3] + 1);
            }
            
            if (i - n >= x) {
                counts[i] = (int) Math.min(counts[i], counts[i-n] + 1);
            }
        }
        

        return counts[y] == 1_000_001 ? -1 : counts[y];
        
    }
}