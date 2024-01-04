import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        Deque<int[]> stack = new LinkedList<>();
        
        for (int i = 0; i < prices.length; i++) {
            while(!stack.isEmpty() && stack.peekLast()[0] > prices[i]) {
                int[] xi = stack.pollLast();
                answer[xi[1]] = i - xi[1];
            }
            stack.addLast(new int[]{prices[i], i});
        }
        
        for (int[] xi : stack) {
            answer[xi[1]] = prices.length - xi[1] - 1;
        }
        
        return answer;
    }
}