class Solution {
    public long solution(int r1, int r2) {
        long r12 = (long) r1 * r1;
        long r22 = (long) r2 * r2;
        long answer = 0;
        
        for (int x = 1; x < r1; x++) {
            long x2 = (long)x*x;
            int r1Max = (int) Math.ceil(Math.sqrt(r12 - x2));
            int r2Max = (int) Math.sqrt(r22 - x2);
                
            answer += r2Max - r1Max + 1;

        }
        
        for (int x = r1; x < r2; x++) {
            long x2 = (long)x*x;
            int r2Max = (int) Math.sqrt(r22 - x2);
            answer += r2Max;
        }
        
        answer += r2 - r1 + 1;
        
        return answer * 4;
    }
}