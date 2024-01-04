import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> counter = new HashMap<>();
        for (String[] c : clothes) {
            counter.merge(c[1], 1, (o, v) -> o + 1);
        }
        int answer = 1;
        for (int v : counter.values()) {
            answer *= v + 1;
        }
        
        return answer -= 1;
    }
}