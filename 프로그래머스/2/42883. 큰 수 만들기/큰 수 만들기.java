import java.util.*;

class Solution {
    public String solution(String number, int k) {
        Deque<Character> stack = new ArrayDeque<>();
            
        stack.push(number.charAt(0));
        
        for (int i = 1; i < number.length(); i++) {
            while (!stack.isEmpty() && k > 0 && stack.peek() < number.charAt(i)) {
                stack.pop();
                k--;
            }
            stack.push(number.charAt(i));
        }
        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        String answer = sb.reverse().toString();
        
        return k == 0 ? answer : answer.substring(0, answer.length() - k);
    }
}