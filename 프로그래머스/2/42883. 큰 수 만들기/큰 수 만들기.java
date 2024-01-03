import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String number, int k) {
        Deque<Character> stack = new LinkedList<>();
        
        for (char c : number.toCharArray()) {
            while (!stack.isEmpty() && stack.peekLast() < c && k > 0) {
                stack.pollLast();
                k--;
            }
            stack.addLast(c);
        }
        String result = stack.stream()
                .map(String::valueOf)
                .collect(Collectors.joining());
        
        return k == 0 ? result : result.substring(0, result.length() - k);
    }
}