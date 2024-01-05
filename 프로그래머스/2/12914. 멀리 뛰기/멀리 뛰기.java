class Solution {
    public long solution(int n) {
        long a = 1;
        long b = 1;
        
        for (int i = 2; i <= n; i++) {
            long temp = b;
            b = (a + b) % 1234567;
            a = temp;
        }
        
        return b;
    }
}