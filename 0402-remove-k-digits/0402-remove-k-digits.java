class Solution {
    public String removeKdigits(String num, int k) {
        // k > 0 이고, stack[top] > n 이면 제거

        char[] stack = new char[num.length()];
        int top = 0;
        char[] ch = num.toCharArray();
        
        for (int i = 0; i < ch.length; i++) {
            char n = ch[i];

            while (top > 0 && k > 0 && stack[top - 1] > n) {
                top--;
                k--;
            }
            stack[top++] = n;
        }

        int start = 0;

        while (k > 0) {
            top--;
            k--;
        }

        while (stack[start] == '0') {
            start++;
        }
        StringBuilder sb = new StringBuilder();
        for(int i = start; i < top; i++) {
            sb.append(stack[i]);
        }
        return sb.isEmpty() ? "0" : sb.toString();
    }
}