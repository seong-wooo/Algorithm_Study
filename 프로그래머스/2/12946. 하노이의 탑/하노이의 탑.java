import java.util.*;
import java.util.stream.*;

class Solution {
    public int[][] solution(int n) {
        return hanoi(1,3,n).stream().toArray(int[][]::new);
    }
    
    public List<int[]> hanoi(int a, int b, int n) {
        if (n == 1) {
            return List.of(new int[]{a, b});
        }
        
        List<int[]> h = new ArrayList<>();
        h.addAll(hanoi(a, 6-a-b, n-1));
        h.addAll(hanoi(a, b, 1));
        h.addAll(hanoi(6-a-b, b, n-1));
        
        return h;
    }
}