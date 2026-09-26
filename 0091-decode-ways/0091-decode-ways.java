class Solution {
    public int numDecodings(String s) {
        int[] dp = new int[s.length() + 1];
        char start = s.charAt(0);
        if (start == '0') {
            return 0;
        }
        dp[0] = 1;
        dp[1] = 1;
        char[] ch = s.toCharArray();
        
        for (int i = 1; i < ch.length; i++) {
            char c = ch[i];

            if (c == '0') {
                if (ch[i-1] != '1' && ch[i-1] != '2') {
                    return 0;
                }

                dp[i + 1] = dp[i-1];
            } else {
                dp[i + 1] = dp[i];

                if ('1' <= c && c <= '6') {
                    if (ch[i-1] == '1' || ch[i-1] == '2') {
                        dp[i+1] += dp[i-1];
                    }
                } else {
                    if (ch[i-1] == '1') {
                        dp[i+1] += dp[i-1];
                    }
                }
            }
        }

        return dp[s.length()];

    }
}