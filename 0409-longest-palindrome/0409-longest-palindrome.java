class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> counter = new HashMap<>();
        for (char c : s.toCharArray()) {
            counter.merge(c, 1, (o, v) -> o + 1);
        }

        int result = 0;
        boolean added = false;
        for (int v : counter.values()) {
            if (v % 2 == 0) {
                result += v;
            } else {
                if (!added) {
                    result += v;
                    added = true;
                } else { 
                    result += v - 1;
                }
            }
        }
        return result;
    }
}