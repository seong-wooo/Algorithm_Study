class Solution {
    public int maxVowels(String s, int k) {
        int answer = 0;
        int current = 0;
        char[] cs = s.toCharArray();
        boolean[] vowel = new boolean[26];
        vowel['a' - 'a'] = true;
        vowel['e' - 'a'] = true;
        vowel['i' - 'a'] = true;
        vowel['o' - 'a'] = true;
        vowel['u' - 'a'] = true;

        for (int i = 0; i < cs.length; i++) {
            if (vowel[cs[i] - 'a']) {
                current++;
            }
            if (i >= k && vowel[cs[i - k] - 'a']) {
                current--;
            }
            answer = Math.max(current, answer);
        }

        return answer;
    }
}