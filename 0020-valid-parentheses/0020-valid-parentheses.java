class Solution {
    public boolean isValid(String s) {
        char[] stack = new char[s.length()];
        int top = 0;

        for (char c : s.toCharArray()) {
            if (c == ')' || c == ']' || c == '}') {
                if (top == 0 || ((c == ')' && stack[top-1] != '(') || (c == ']' && stack[top-1] != '[') || (c == '}' && stack[top-1] != '{'))) {
                    return false;
                }
                top--;
            } else {
                stack[top++] = c;
            }
        }
        return top == 0;
    }
}