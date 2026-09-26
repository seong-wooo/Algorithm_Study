class Solution {
    public int numDecodings(String s) {
        int[] dp = new int[s.length() + 1];
        if (s.charAt(0) == '0') {
            return 0;
        }

        dp[0] = 1;
        dp[1] = 1;

        char[] ch = s.toCharArray();
        for (int i = 2; i < ch.length + 1; i++) {
            int one = ch[i-1] - '0';
            int two = (ch[i-2] - '0') * 10 + one;

            if (one != 0) {
                dp[i] += dp[i-1];
            }

            if (10 <= two && two <= 26) {
                dp[i] += dp[i-2];
            }
        }
        
        return dp[dp.length - 1];
    }
}