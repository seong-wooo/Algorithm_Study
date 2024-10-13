import java.util.*;

class Solution {
    public String[] solution(String[][] tickets) {
        Map<String, PriorityQueue<String>> path = new HashMap<>();
        
        for (String[] ticket : tickets) {
            path.putIfAbsent(ticket[0], new PriorityQueue<>());
            path.get(ticket[0]).add(ticket[1]);
        }  
        
        List<String> answer = new LinkedList<>();
        Deque<String> stack = new ArrayDeque<>();
        
        stack.push("ICN");
        
        while(!stack.isEmpty()) {
            while (path.containsKey(stack.peek()) && !path.get(stack.peek()).isEmpty()) {
                stack.push(path.get(stack.peek()).poll());
            }
            
            answer.add(0, stack.pop());
        }
        return answer.toArray(new String[0]);
    }
}