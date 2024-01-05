class Solution {
    public int solution(int n) {
        int one = countOne(n);
        n++;
        while (countOne(n) != one) {
            n++;
        }
        
        return n;
    }
    
    public int countOne(int n) {
        String a = Integer.toBinaryString(n);
        int one = 0;
        for (char o : a.toCharArray()) {
            if (o == '1') {
                one++;
            }
        }
        return one;
    }
    
}