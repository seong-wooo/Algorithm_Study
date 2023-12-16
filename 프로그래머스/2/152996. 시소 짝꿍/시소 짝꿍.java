import java.util.*;

class Solution {
    public long solution(int[] weights) {
        Map<Integer, Integer> maps = new HashMap<>();
        
        for (int weight : weights) {
            maps.merge(weight, 1, (o, v) -> o + 1);
        }
    
        
        long answer = 0;
        for (Map.Entry<Integer, Integer> kv : maps.entrySet()) {
            int key = kv.getKey();
            int value = kv.getValue();
            
            answer += (long) value * (value - 1) / 2;
            
            if ( (key / 2.0) % 1 == 0 && maps.containsKey(key * 3 / 2)) {
                answer += (long) value * maps.get(key * 3 / 2);
            }
            if (maps.containsKey(key * 2)) {
                answer += (long) value * maps.get(key * 2);
            }
            if ( (key / 3.0) % 1 == 0 && maps.containsKey(key * 4 / 3)) {
                answer += (long) value * maps.get(key * 4 / 3);
            }
        }    
        return answer;
    }
}