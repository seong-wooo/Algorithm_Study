class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        Map<Character, Character> matching = Map.of(
            '}', '{', 
            ']', '[',
            ')', '('
        );

        for (char c : s.toCharArray()) {
            if (!matching.containsKey(c)) {
                stack.push(c);
            } else {
                if (stack.isEmpty() || stack.pop() != matching.get(c)) {
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
}