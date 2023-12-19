class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int gcdA = arrayA[0];
        for (int a : arrayA) {
            gcdA = gcd(gcdA, a);
        }
        
        int gcdB = arrayB[0];
        for (int b : arrayB) {
            gcdB = gcd(gcdB, b);
        }
        
        
        if (gcdA == 1 && gcdB == 1) {
            return 0;
        }

        
        int answer = gcdA;
        for (int b : arrayB) {
            if (b % gcdA == 0) {
                answer = 0;
                break;
            }
        }
        
        if (answer > gcdB) {
            return answer;
        }
        
        answer = gcdB;
        for (int a : arrayA) {
            if (a % gcdB == 0) {
                answer = 0;
                break;
            }
        }
        
        return answer;
    }
    
    public int gcd(int a, int b) {
        if (b > a) {
            int temp = b;
            b = a;
            a = temp;
        }
        
        return b == 0 ? a : gcd(b, a % b);
    }
}