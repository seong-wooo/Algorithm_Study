import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(String s) {
        Map<Integer, Integer> counter = new HashMap<>();
        
        String[] digits = s.replace("{{", "").replace("}}", "").split("\\},\\{");
        
        for (String digit : digits) {
            String[] d = digit.split(",");
            for (String x : d) {
                counter.merge(Integer.valueOf(x), 1, (o, v) -> o + 1);
            }
        }
    
        
        return counter.entrySet().stream()
            .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
            .mapToInt(Map.Entry::getKey)
            .toArray();

    }
}