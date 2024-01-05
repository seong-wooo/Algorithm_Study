class Solution {
    public int solution(int n) {
        int one = Integer.bitCount(n);
        n++;
        while (Integer.bitCount(n) != one) {
            n++;
        }
        
        return n;
    }
}