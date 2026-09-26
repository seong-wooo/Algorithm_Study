class Solution {
    public String minRemoveToMakeValid(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        boolean[] removed = new boolean[s.length()];

        char[] ch = s.toCharArray();

        for(int i = 0; i < ch.length; i++) {
            char c = ch[i];

            if (c == '(') {
                stack.push(i);
            } else if (c == ')') {
                if (stack.isEmpty()) {
                    removed[i] = true;
                } else {
                    stack.pop();
                }
            }
        }

        for (int index : stack) {
            removed[index] = true;
        }
        StringBuilder sb = new StringBuilder(ch.length);
        for(int i = 0; i < ch.length; i++) {
            if(!removed[i]) {
                sb.append(ch[i]);
            }
        }
        return sb.toString();
    }
}