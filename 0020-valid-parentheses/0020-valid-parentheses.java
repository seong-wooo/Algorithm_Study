class Solution {
    public boolean isValid(String s) {
        char[] stack = new char[s.length()];
        int top = 0;

        for (char c : s.toCharArray()) {
            if (c == ')') {
                if (top == 0 || stack[top-1] != '(') {
                    return false;
                }
                top--;
            } else if (c == ']') {
                if (top == 0 || stack[top-1] != '[') {
                    return false;
                }
                top--;
            } else if (c == '}') {
                if (top == 0 || stack[top-1] != '{') {
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