class Solution {
    public String decodeString(String s) {
        Deque<StringBuilder> stackSB = new ArrayDeque<>();
        Deque<Integer> stackCT = new ArrayDeque<>();
        StringBuilder cur = new StringBuilder();
        int k = 0;

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                k = 10 * k + c - '0';
            } else if (c == '[') {
                stackCT.push(k);
                stackSB.push(cur);
                cur = new StringBuilder();
                k = 0;
            } else if (c == ']') {
                StringBuilder prev = stackSB.pop();
                prev.append(cur.toString().repeat( stackCT.pop()));
                cur = prev;
            } else {
                cur.append(c);
            }
        }

        return cur.toString();
    }
}