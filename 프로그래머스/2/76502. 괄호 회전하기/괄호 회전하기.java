import java.util.*;

class Solution {
    public int solution(String s) {
        
        s = s.replace("(", "0").replace(")", "1").replace("[", "2").replace("]", "3").replace("{", "4").replace("}", "5");
        
        int answer = 0;
        
        for (int i = 0; i < s.length(); i++) {
            s = s.substring(1) + s.charAt(0);
            answer += exec(s);
        }
        
        return answer;
    }
    
    public int exec(String s) {
        Deque<Integer> stack = new LinkedList<>();
        
        for (int i = 0; i < s.length(); i++) {     
            char c = s.charAt(i);
            if (c == '1' || c == '3' || c == '5') {
                int target = Integer.valueOf(c) - 1;
                if (stack.isEmpty() || stack.peekLast() != target){
                    return 0;
                }
                stack.pollLast();
            } else {
                stack.add(Integer.valueOf(c));
            }
        }
        
        if (stack.isEmpty()) {
            return 1;
        }
        return 0;
    }
}