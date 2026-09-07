import java.util.*;

class Solution {
    public int trap(int[] height) {
        Deque<Integer> stack = new ArrayDeque<>();
        int answer = 0;

        for (int i = 0; i < height.length; i++) {
            while(!stack.isEmpty() && height[i] > height[stack.peek()]) {
                int before = stack.pop();

                if (stack.isEmpty()) {
                    break;
                }

                int distance = i - stack.peek() - 1;

                int waters = Math.min(height[i], height[stack.peek()]) - height[before];

                answer += distance * waters;
            }
            stack.push(i);
        }
        return answer;
    }
}