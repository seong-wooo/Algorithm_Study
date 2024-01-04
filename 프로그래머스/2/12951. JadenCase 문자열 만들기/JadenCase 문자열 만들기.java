import java.util.*;

class Solution {
    public String solution(String s) {
        char[] c = s.toCharArray();
        
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(c[i])) {
                if (i == 0 || i > 0 && c[i - 1] == ' ') {
                    c[i] = Character.toUpperCase(c[i]);   
                } else {
                    c[i] = Character.toLowerCase(c[i]);
                }
            }
            
        }
        
        StringBuilder sb = new StringBuilder();
        
        for (char a : c) {
            sb.append(a);
        }
        return sb.toString();
    }
}