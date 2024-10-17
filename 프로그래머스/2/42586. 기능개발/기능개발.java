import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] days = new int[speeds.length];
        
        for (int i = 0; i < speeds.length; i++) {
            days[i] = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
        }
        
        int i = 0;
        List<Integer> answer = new ArrayList<>();
        while (i < days.length) {
            int j = i + 1;
            
            while (j < days.length && days[i] >= days[j]) {
                j++;
            }
            answer.add(j - i);
            i = j;
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
