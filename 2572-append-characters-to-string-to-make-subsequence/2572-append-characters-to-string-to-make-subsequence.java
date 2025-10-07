class Solution {
    public int appendCharacters(String s, String t) {
        int t_index = 0;

        for (char c : s.toCharArray()) {
            if (t_index == t.length()) {
                return 0;
            }
            if (t.charAt(t_index) == c) {
                t_index++;
            }
        }

        return t.length() - t_index;
    }
}