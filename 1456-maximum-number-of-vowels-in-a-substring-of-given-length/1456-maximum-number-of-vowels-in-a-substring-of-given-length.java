class Solution {
    public int maxVowels(String s, int k) {
        boolean[] m = new boolean[26];
        m[0] = true;
        m['e'-'a'] = true;
        m['i'-'a'] = true;
        m['o'-'a'] = true;
        m['u'-'a'] = true;


        int answer = 0;
        char[] ch = s.toCharArray();
        for (int i = 0; i < k; i++) {
            if (m[ch[i] - 'a']) {
                answer++;
            }
        }
        
        int current = answer;
        for (int i = k; i < ch.length; i++) {
            if (m[ch[i - k] - 'a']) {
                current--;
            }

            if (m[ch[i] - 'a']) {
                current++;
            }
            answer = (int) Math.max(answer, current);
        }

        return answer;
    }
}