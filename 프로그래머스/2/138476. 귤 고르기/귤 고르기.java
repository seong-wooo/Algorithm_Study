import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> counter = new HashMap<>();
        
        for (int tang : tangerine) {
            counter.merge(tang, 1, (o,v) -> o+1);
        }
        
        int answer = counter.keySet().size();
        
        List<Integer> c = counter.entrySet()
                                .stream()
                                .map(kv -> kv.getValue())
                                .sorted(Comparator.reverseOrder())
                                .collect(Collectors.toList());
        
        for (int i = 0; i < c.size(); i++) {        
            if (k <= 0) {
                return i;
            }
            
            k -= c.get(i);
        }
        
        
        return c.size();
    }
}