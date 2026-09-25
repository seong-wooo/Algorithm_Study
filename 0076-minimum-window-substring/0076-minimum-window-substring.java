class Solution {
    public String minWindow(String s, String t) {
        if (t.length() > s.length()) {
            return "";
        }

        int[] counter = new int[128];
        int missing = 0;
        for (char c : t.toCharArray()) {
            if (counter[c]++ == 0) {
                missing++;
            }
        }

        int left = 0;
        int minSize = Integer.MAX_VALUE;
        int bestLeft = 0;

        char[] ch = s.toCharArray();

        for (int right = 0; right < ch.length; right++) {
            if (--counter[ch[right]] == 0) {
                missing--;
            }

            while (missing == 0) {
                if (right - left + 1 < minSize) {
                    minSize = right - left + 1; 
                    bestLeft = left;
                }
                if (++counter[ch[left]] == 1) {
                    missing++;
                }
                left++;
            }
        }

        return minSize == Integer.MAX_VALUE ? "" : s.substring(bestLeft, bestLeft + minSize);

    }
}   