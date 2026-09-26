class Solution {
    public String minRemoveToMakeValid(String s) {
        Set<Integer> removeIndex = new HashSet<>();

        Deque<Integer> stack = new ArrayDeque<>();

        char[] ch = s.toCharArray();

        for(int i = 0; i < ch.length; i++) {
            char c = ch[i];

            if (c == '(') {
                stack.push(i);
            } else if (c == ')') {
                if (stack.isEmpty()) {
                    removeIndex.add(i);
                } else {
                    stack.pop();
                }
            }
        }

        for (int index : stack) {
            removeIndex.add(index);   
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < ch.length; i++) {
            if (!removeIndex.contains(i)) {
                sb.append(ch[i]);
            }
        }
        return sb.toString();
    }
}