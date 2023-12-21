import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        Map<String, Integer> w = new HashMap<>();
        
        for (int i = 0; i < want.length; i++) {
            w.put(want[i], number[i]);
        }
        Map<String, Integer> d = new HashMap<>();
        
        for (int i = 0; i < 10; i++) {
            d.merge(discount[i], 1, (o, v) -> o + 1);
        }
        int result = contains(w, d);
        
        for (int i = 1; i < discount.length - 9; i++) {
            d.computeIfPresent(discount[i - 1], (k, v) -> v - 1);
            if (d.get(discount[i - 1]) == 0) {
                d.remove(discount[i - 1]);
            }
            d.merge(discount[i + 9], 1, (o, v) -> o + 1);
            
            result += contains(w, d);
        }
        return result;
        
    }
    
    public int contains(Map<String, Integer> w, Map<String, Integer> d) {
        for (Map.Entry<String, Integer> v : w.entrySet()) {
            if (!d.containsKey(v.getKey()) || v.getValue() > d.get(v.getKey())) {
                return 0;
            }
        }
        return 1;
    }
}