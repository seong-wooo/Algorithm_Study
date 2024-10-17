import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        Set<String> pre = new HashSet<>();
        pre.add(words[0]);
        
        for (int i = 1; i < words.length; i++) {
            if (pre.contains(words[i]) || words[i-1].charAt(words[i-1].length() - 1)  != words[i].charAt(0)) {
                return new int[] {i % n + 1, i / n + 1};
            }
            pre.add(words[i]);
        }
        
        return new int[]{0,0};
    }
}