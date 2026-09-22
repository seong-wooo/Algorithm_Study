class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0;
        char[] ch = s.toCharArray();
        int[] counter = new int[26];
        
        int maxCount = 0;

        for (int right = 0; right < ch.length; right++) {
            int index = ch[right] - 'A';

            maxCount = Math.max(++counter[index], maxCount);


            if (right - left + 1 - k > maxCount) {
                counter[ch[left++] - 'A']--;
            }
        }
        return ch.length - left;
    }
}