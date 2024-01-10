import java.util.*;

class Solution {
    public int solution(String name) {
        int answer = name.length() - 1;
        int total = 0;
        for (char c : name.toCharArray()) {
            total += move(c);
        }
        int i = 0;
        
        while (i < name.length()) {
            int j = i + 1;
            while (j < name.length() && name.charAt(j) == 'A') {
                j++;
            }
            
            if (j == name.length()) {
                answer = (int) Math.min(answer, i);
            } else {
                answer = (int) Math.min(answer, (int) Math.min(i * 2 + name.length() - j, (name.length() - j) * 2 + i));
            }
            i = j;
        }
        
        return answer + total;
    }
    
    public int move(char c) {
        int n = Integer.valueOf(c);
        return (int) Math.min(n - 65, 91 - n);
    }
    
}