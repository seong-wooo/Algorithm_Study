import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(String numbers) {
        char[] c = numbers.toCharArray();
        Arrays.sort(c);
        
        StringBuilder sb = new StringBuilder();
        
        for (int i = c.length-1; i >= 0; i--) {
            sb.append(c[i]);
        }
        int m = Integer.valueOf(sb.toString());
        
        boolean[] sosu = new boolean[m + 1];
        Arrays.fill(sosu, true);
        sosu[0] = false;
        sosu[1] = false;
        
        for (int i = 2; i < sosu.length; i++) {
            if (sosu[i]) {
                for (int j = i * 2; j < sosu.length; j += i) {
                    sosu[j] = false;
                }
            }
        }
        int answer = 0;
        
        Set<Integer> pers = new HashSet<>();
        getPermutations(numbers, "", pers);
        
        for (int p : pers) {
            if (sosu[p]) {
                answer++;
            }
        }
    
        return answer;
    }
    
    public void getPermutations(String numbers, String str, Set<Integer> pers) {
        if (!str.isEmpty()) {
            pers.add(Integer.valueOf(str));
        }
        
        for (int i = 0; i < numbers.length(); i++) {
            getPermutations(numbers.substring(0, i) + numbers.substring(i+1), str + numbers.charAt(i), pers);
        }
    }
}