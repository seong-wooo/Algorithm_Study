class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        char[] ch = new char[128];
        int answer = 0;
        for (int right = 0; right < s.length(); right++) {
            char c  = s.charAt(right);
            ch[c]++;
            while (ch[c] > 1) {
                ch[s.charAt(left++)]--;
            }
            answer = Math.max(answer,right - left + 1);
        }
        return answer;
    }
}