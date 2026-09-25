class Solution {
    public int characterReplacement(String s, int k) {
        int most = 0;
        int[] counter = new int[28];
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            counter[c - 'A']++;

            most = Math.max(most, counter[c - 'A']);

            if (right - left + 1 - most > k) {
                counter[s.charAt(left++) -  'A']--;
            }
        }
        return s.length() - left;
    }
}