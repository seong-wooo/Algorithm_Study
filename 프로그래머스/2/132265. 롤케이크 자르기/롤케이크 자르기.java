import java.util.*;

class Solution {
    public int solution(int[] topping) {
        Map<Integer, Integer> rightCounter = new HashMap<>();
        
        for (int t : topping) {
            rightCounter.merge(t, 1, (o,v) -> o + 1);
        }
        
        Map<Integer, Integer> leftCounter = new HashMap<>();
        int answer = 0;
        for (int t : topping) {
            rightCounter.computeIfPresent(t, (k, v) -> v - 1);
            if (rightCounter.get(t) == 0) {
                rightCounter.remove(t);
            }
            leftCounter.merge(t, 1, (o, v) -> o + 1);
            
            if (rightCounter.size() == leftCounter.size()) {
                answer++;
            }
        }
        return answer;
    }
}