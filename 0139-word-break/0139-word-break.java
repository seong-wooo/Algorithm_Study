class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        
        Set<String> dict = new HashSet<>(wordDict);

        int n = s.length();
        boolean[] word = new boolean[n + 1];
        word[0] = true;

        for (int i = 0; i < n; i++) {
            for(int k = 0; k < i + 1; k++) {
                if (word[k]) {
                    if (dict.contains(s.substring(k, i + 1))) {
                        word[i + 1] = true;
                        continue;
                    }
                }
            }
        }

        return word[n];
    }
}