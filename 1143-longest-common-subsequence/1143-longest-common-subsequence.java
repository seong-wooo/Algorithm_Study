class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();

        int[][] mn = new int[m+1][n+1];

        for (int j = 1; j < m + 1; j++) {
            for (int i = 1; i < n+1; i++) {
                if (text1.charAt(j - 1) == text2.charAt(i - 1)) {
                    mn[j][i] = mn[j-1][i-1] + 1;
                } else {
                    mn[j][i] = Math.max(mn[j-1][i], mn[j][i-1]);
                }
            }
        }

        return mn[m][n];
    }
}