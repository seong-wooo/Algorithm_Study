import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] order) {
        Deque<Integer> stack = new LinkedList<>();
        Queue<Integer> belt = IntStream.rangeClosed(1, order.length).boxed().collect(Collectors.toCollection(LinkedList::new));
        
        int i = 0;
        
        while (i < order.length) {
            int o = order[i];
            if (!belt.isEmpty() && belt.peek() == o) {
                belt.poll();
                i++;
            } else if (!stack.isEmpty() && stack.peekLast() == o) {
                stack.pollLast();
                i++;
            } else {
                if (!belt.isEmpty()) {
                    stack.add(belt.poll());
                } else {
                    break;
                }
            }
        }
        
        return i;
        
    }
}