class Solution {
    public String solution(int n, int t, int m, int p) {
        int maxLength = m * (t - 1) + p;
        
        String base = "";
        int num = 0;
        while (base.length() < maxLength) {
            base += Integer.toString(num++, n);
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = p - 1; i < maxLength; i += m) {
            sb.append(base.charAt(i));
        }
        return sb.toString().toUpperCase();
    }
}