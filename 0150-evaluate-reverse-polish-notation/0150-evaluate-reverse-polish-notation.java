class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();

        for(String token : tokens) {
            if (Character.isDigit(token.charAt(token.length() -1 ))) {
                stack.push(Integer.parseInt(token));
            } else {
                int a = stack.pop();
                int b = stack.pop();

                switch(token.charAt(0)) {
                    case '*': 
                        stack.push(a*b);
                        break;
                    case '+': 
                        stack.push(a+b);
                        break;
                    case '-': 
                        stack.push(b-a);
                        break;
                    default : 
                        stack.push(b/a);
                }
            }
        }
        return stack.pop();
    }
}