class Solution {
    public int solution(int n) {
        int a = 0;
        int b = 1;
        
        for (int i = 0; i < n - 1; i++) {
            int temp = b;
            b = (a + b) % 1234567 ;
            a = temp;
        }
        
        return b;
    }
}