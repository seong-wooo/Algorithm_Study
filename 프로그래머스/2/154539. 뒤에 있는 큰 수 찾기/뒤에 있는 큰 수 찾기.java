import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Arrays.fill(answer, -1);
        Deque<Integer> stack = new LinkedList<>();
        
        for (int i = 0; i < numbers.length; i++) {
            while(!stack.isEmpty() && numbers[stack.peekLast()] < numbers[i]) {
                answer[stack.pollLast()] = numbers[i];
            }
            stack.add(i);
            
        }
        
        
        
        
        return answer;
    }
}