class Solution {
    public String solution(int n, int t, int m, int p) {
        String[] arr = new String[16];
        for (int i = 0; i < 10; i++) {
            arr[i] = String.valueOf(i);
        }
        
        arr[10] = "A";
        arr[11] = "B";
        arr[12] = "C";
        arr[13] = "D";
        arr[14] = "E";
        arr[15] = "F";
        int maxLength = m * (t - 1) + p;
        
        String base = "";
        int num = 0;
        while (base.length() < maxLength) {
            base += toN(num, n, arr);
            num++;
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = p - 1; i < maxLength; i += m) {
            sb.append(base.charAt(i));
        }
        return sb.toString();
    }
    
    public String toN(int num, int n, String[] arr) {    
        StringBuilder sb = new StringBuilder();
        while (num >= n) {
            sb.append(String.valueOf(arr[num % n]));
            num /= n;
        }
        sb.append(String.valueOf(arr[num]));
        
        return sb.reverse().toString();
    }
    
}