class Solution {
    public String makeGood(String s) {
        StringBuilder sb = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (!sb.isEmpty() && (sb.charAt(sb.length() - 1) == c - ('a' - 'A') || sb.charAt(sb.length() - 1) == c + ('a' - 'A'))) {
                sb.setLength(sb.length() - 1);
            } else { 
                sb.append(c);
            }
        }

        return sb.toString();
    }
}