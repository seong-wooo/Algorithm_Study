class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> index = new HashMap<>();
        int answer = 0;
        char[] ch = s.toCharArray();
        int left = 0;
        int current = 0;

        for (int right = 0; right < ch.length; right++) {
            Integer prev = index.put(ch[right], right);

            if (prev == null || prev < left) {
                answer = (int) Math.max(answer, right - left + 1);
            } else {
                left = prev + 1;
            }
        }

        return answer;
    }
}