class Solution {
    public String reorganizeString(String s) {
        int n = s.length();
        int[] counter = new int[26];
        int max = 0;

        for (char c : s.toCharArray()) {
            counter[c - 'a']++;
            if (counter[c - 'a'] > counter[max]) {
                max = c - 'a';
            }
        }
        if (counter[max] > (n + 1) / 2) {
            return "";
        }

        char[] result = new char[n];
        int idx = 0;

        idx = fill(result, idx, max, counter[max], n);   // 최빈 글자를 먼저
        counter[max] = 0;

        for (int i = 0; i < 26; i++) {
            idx = fill(result, idx, i, counter[i], n);
        }
        return new String(result);
    }

    private int fill(char[] result, int idx, int letter, int freq, int n) {
        for (int k = 0; k < freq; k++) {
            result[idx] = (char) ('a' + letter);
            idx += 2;
            if (idx >= n) {
                idx = 1;          // 짝수 자리를 다 쓰면 홀수 자리로 넘어간다
            }
        }
        return idx;
    }
}