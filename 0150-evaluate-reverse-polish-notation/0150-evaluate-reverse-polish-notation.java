class Solution {
    public int evalRPN(String[] tokens) {
        int[] stack = new int[tokens.length];
        int top = 0;

        for(String token : tokens) {
            switch (token) {
                case "*" -> {int r = stack[--top]; stack[top-1] *= r; }
                case "+" ->  {int r = stack[--top]; stack[top-1] += r; }
                case "-" ->  {int r = stack[--top]; stack[top-1] -= r; }
                case "/" ->  {int r = stack[--top]; stack[top-1] /= r; }
                default -> stack[top++] = Integer.parseInt(token);
                
            }
        }
        return stack[0];
    }
}