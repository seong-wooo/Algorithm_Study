import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        
        int[] d = new int[speeds.length];
        
        for (int i = 0; i < speeds.length; i++) {
            d[i] = (int) Math.ceil((100 - progresses[i]) / (double) speeds[i]);
        }
        
        int i = 0;
        
        while (i < d.length) {
            int result = 1;
            int n = d[i];
            i++;
            while (i < d.length && n >= d[i]) {
                i++;
                result++;
            }
            answer.add(result);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}