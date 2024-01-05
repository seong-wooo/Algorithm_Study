class Solution {
    public int solution(int n) {
        long a = 1;
        long b = 2;
        
        for (int i = 3; i <= n; i++) {
            long temp = b;
            b = (a + b) % 1000000007;
            a = temp;
        }
        
        return (int) b;
    }
}