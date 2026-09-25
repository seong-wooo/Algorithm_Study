class Solution {
    public int characterReplacement(String s, int k) {
        int most = 0;
        Map<Character, Integer> counter = new HashMap<>();
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            counter.merge(c, 1, Integer::sum);

            most = Math.max(most, counter.get(c));

            if (right - left + 1 - most > k) {
                counter.put(s.charAt(left), counter.get(s.charAt(left++)) - 1);
            }
        }
        return s.length() - left;
    }
}