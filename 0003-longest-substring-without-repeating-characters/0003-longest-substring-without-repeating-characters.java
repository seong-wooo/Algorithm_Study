class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> used = new HashMap<>();

        int answer = 0;
        int left = 0;
        int right = 0;

        while (right < s.length()) {
            char c = s.charAt(right);
            if (used.containsKey(c) && used.get(c) >= left) {
                left = used.get(c) + 1;
            }
            used.put(c, right);
            answer = (int) Math.max(answer, right - left + 1);
            right++;
        }
        return answer;
    }
}