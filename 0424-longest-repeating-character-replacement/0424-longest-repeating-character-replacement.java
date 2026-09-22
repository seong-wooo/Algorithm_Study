class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0;
        char[] ch = s.toCharArray();
        int[] counter = new int[26];

        char maxAlpha = ' ';
        int maxCount = 0;
        int answer = 0;

        for (int right = 0; right < ch.length; right++) {
            int index = ch[right] - 'A';

            counter[index]++;
            
            if (counter[index] > maxCount) {
                maxCount = counter[index];
                maxAlpha = ch[right];
            }

            if (right - left + 1 - k > maxCount) {
                counter[ch[left] - 'A']--;
                if (ch[left] == maxAlpha) {
                    for (int i = left + 1; i <= right; i++) {
                        if (counter[ch[i] - 'A'] > maxCount) {
                            maxCount = counter[ch[i] - 'A'];
                            maxAlpha = ch[i];
                        }
                    }
                }
                left++;
            }

            answer = Math.max(answer, right - left + 1);
        }
        return answer;
    }
}