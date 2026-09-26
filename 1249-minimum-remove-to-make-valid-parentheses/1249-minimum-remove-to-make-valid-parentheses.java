class Solution {
    public String minRemoveToMakeValid(String s) {
        char[] ch = s.toCharArray();
        StringBuilder sb = new StringBuilder(s.length());
        int open = 0;
        for(int i = 0; i < ch.length; i++) {
            char c = ch[i];
            if (c == '(') {
                open++;
                sb.append(c);
            } else if (c == ')') {
                if (open == 0) {
                    continue;
                } 
                open--;
                sb.append(c);
            } else {
                sb.append(c);
            }   
        }

        StringBuilder result = new StringBuilder(sb.length());
        for (int i = sb.length() - 1; i  >= 0; i--) {
            char c = sb.charAt(i);

            if (c == '(') {
                if (open > 0) {
                    open--;
                    continue;
                }
            }   
            result.append(c);
        }

        return result.reverse().toString();
    }
}