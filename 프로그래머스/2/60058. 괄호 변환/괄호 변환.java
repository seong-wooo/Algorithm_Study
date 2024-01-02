import java.util.*;

class Solution {
    public String solution(String p) {
        if (p.isEmpty() || isCorrect(p)) {
            return p;
        }
        
        int cnt = 0;
        String u = "";
        String v = "";
        
        for(int i = 0; i < p.length(); i ++){
            if(p.charAt(i) == '(') {
                cnt++;
            }
            else {
              cnt--;  
            } 

            if(cnt == 0){
                u = p.substring(0, i + 1);
                v = p.substring(i + 1);
                break;
            }
        }
        
        if (isCorrect(u)) {
            return u + solution(v);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < u.length() - 1; i++) {
            if (u.charAt(i) == '(') {
                sb.append(")");
            } else {
                sb.append("(");
            }
        }
        
        return "(" + solution(v) + ")" + sb.toString();
    }
    
    public boolean isCorrect(String u) {
        int stack = 0;
        
        for (char c : u.toCharArray()) {
            if (c == '(') {
                stack++;
            } else {
                if (stack == 0) {
                    return false;
                }
                stack--;
            }
        }
        
        return stack == 0;
    }
}