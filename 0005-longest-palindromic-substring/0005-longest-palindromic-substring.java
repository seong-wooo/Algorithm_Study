class Solution {
    int left;
    int right; 

    public String longestPalindrome(String s) {
        for (int i = 0; i < s.length() -1; i++) {
            findPalindrome(s, i, i+1);
            findPalindrome(s, i, i+2);
        }

        return s.substring(left, right + 1);
    }

    private void findPalindrome(String s, int start, int end) {
        while (start >= 0 &&  end < s.length() && s.charAt(start) == s.charAt(end) ) {
            if (right - left < end - start) {
                left = start;
                right = end;
            }

            if (start == 0 || end == s.length() - 1) {
                break;
            }
            start--;
            end++;
        }
    }
}