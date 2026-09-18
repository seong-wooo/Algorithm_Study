class Solution {
    public int countGoodSubstrings(String s) {
        if (s.length() < 3) {
            return 0;
        }

        char[] ch = s.toCharArray();
        int[] freq = new int[26];
        int dup = 0;
        int answer = 0;
        for(int i = 0; i < ch.length; i++) {
            freq[ch[i] - 'a']++;

            if(freq[ch[i] - 'a'] == 2) {
                dup++;
            }

            if (i >= 3) {
                freq[ch[i - 3] - 'a']--;
                if(freq[ch[i - 3] - 'a'] == 1) {
                    dup--;
                }
            }

            if (i >= 2 && dup == 0) {
                answer++;
            }

        }

        return answer;
    }
}