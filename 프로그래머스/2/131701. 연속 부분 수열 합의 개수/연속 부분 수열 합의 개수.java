import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int[] e = new int[elements.length + 1];
        for (int i = 0; i < elements.length; i++) {
            e[i + 1] = e[i] + elements[i];
        }
        
        Set<Integer> answer = new HashSet<>();
        
        for (int left = 0; left < e.length - 1; left++) {
            for (int right = left+1; right < e.length; right++) {
                int total = e[right] - e[left];
                answer.add(total);
                answer.add(e[e.length - 1] - total);
            }
        }
        
        return answer.size() - 1;
    }
}