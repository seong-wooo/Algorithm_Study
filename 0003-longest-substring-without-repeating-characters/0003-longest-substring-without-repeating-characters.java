class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] counter = new int[128];
        int answer = 0;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            counter[s.charAt(right)]++;

            while (counter[s.charAt(right)] == 2) {
                counter[s.charAt(left++)]--;
            }

            answer = Math.max(answer, right - left + 1);
        }
        return answer;
    }
}