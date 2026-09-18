class Solution {
    public int countGoodSubstrings(String s) {
        if (s.length() <= 2) {
            return 0;
        }

        int[] exists = new int[26];
        Arrays.fill(exists, -1);
        boolean first = true;
        for (int i = 0; i < 3; i++) {
            if (exists[index(s, i)] >= 0) {
                first = false;
            }
            
            exists[index(s, i)] = i;
        }
        int answer = first ? 1 : 0;

        for (int i = 3; i < s.length(); i++) {
            if (exists[index(s, i)] < i - 2 && (s.charAt(i - 1) != s.charAt(i-2))) {
                answer++;
            }
            exists[index(s, i)] = i;
        }

        return answer;
    }

    private int index(String s, int i) {
        return s.charAt(i) - 'a';
    }
}