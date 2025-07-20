class Solution {
    public String reverseWords(String s) {
        int left = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 0 ; i < s.length(); i++) {
            if (s.charAt(i) == ' ') { 
                for (int j = i-1; j >= left; j--) {
                    sb.append(s.charAt(j));
                }
                sb.append(' ');
                left = i + 1;
            }
        }
        for (int j = s.length()-1; j >= left; j--) {
            sb.append(s.charAt(j));
        }

        return sb.toString();
    }
}