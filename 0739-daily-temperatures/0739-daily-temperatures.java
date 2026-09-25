class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] stack = new int[temperatures.length];
        int top = 0;
        int[] answer = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {
            while (top > 0 && temperatures[stack[top - 1]] < temperatures[i]) {
                answer[stack[top - 1]] = i - stack[top - 1];
                top--;
            }
            stack[top++] = i;
        }

        while (top > 0) {
            answer[stack[--top]] = 0;
        }

        return answer;
    }
}