class Solution {
    public int maxVowels(String s, int k) {
        int answer = 0;
        int current = 0;
        char[] cs = s.toCharArray();

        for (int i = 0; i < cs.length; i++) {
            if (isVowel(cs[i])) {
                current++;
            }
            if (i >= k && isVowel(cs[i - k])) {
                current--;
            }
            answer = Math.max(current, answer);
        }

        return answer;
    }

    public boolean isVowel(char c) {
        return c == 'a' 
        || c == 'e'
        || c == 'i' 
        || c == 'o'
        || c == 'u';
    }
}