import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        Arrays.sort(data, Comparator.comparingInt((int[] d) -> d[col - 1]).thenComparingInt((d) -> -d[0]));
        
        int result = 0;
        for (int i=row_begin - 1; i < row_end; i++) {
            int[] row = data[i];
            int index = i + 1;
            result ^= Arrays.stream(row).map(d -> d % index).sum();
        }
        
        return result;
    }
}