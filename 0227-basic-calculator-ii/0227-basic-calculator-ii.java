class Solution {
    public int calculate(String s) {
        char op = '+';
        int num = 0;
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0 ; i < s.length(); i++)  { 
            char c = s.charAt(i);

            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            }

            if (!Character.isDigit(c) && c != ' ' || i == s.length() - 1) {
                switch(op) {
                    case('+') -> stack.push(num);
                    case('-') -> stack.push(-num);
                    case('*') -> stack.push(stack.pop() * num);
                    case('/') -> stack.push(stack.pop() / num);
                }
                op = c;
                num = 0;
            }
        }

        int result = 0;
        for (int a : stack) {
            result += a;
        }
        return result;
    }
}