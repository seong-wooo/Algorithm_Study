class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] last = new int[128];
        Arrays.fill(last, -1);
        int answer = 0;
        int left = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            left = Math.max(left, last[c] + 1);
            answer = Math.max(i - left + 1, answer);
            last[c] = i;
        }
        return answer;
    }
}