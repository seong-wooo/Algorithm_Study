class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] count = new int[26];

        for (int i = 0; i < s1.length(); i++) {
            count[s1.charAt(i) - 'a']++;
        }

        int left = 0;
        for (int right = 0; right < s2.length(); right++) {
            char c = s2.charAt(right);
            count[c - 'a']--;

            while(count[c - 'a'] < 0) {
                count[s2.charAt(left++) - 'a']++;
            }

            if (right - left + 1 == s1.length()) {
                return true;
            }
        }
        return false;
    }
}