class Solution {
    public boolean isAnagram(String s, String t) {
        int[] counter = new int[26];

        if (s.length() != t.length()) {
            return false;
        }

        for (char c : s.toCharArray()) {
            counter[c - 'a']++;
        }

        for (char c : t.toCharArray()) {
            counter[c - 'a']--;
            if (counter[c - 'a'] < 0) {
                return false;
            }
        }   
        return true;
    }
}