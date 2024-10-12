class Solution {
    public long solution(int r1, int r2) {
        long r12 = (long) r1 * r1;
        long r22 = (long) r2 * r2;
        long answer = r2-r1+1;
        for (long x=1; x<r1; x++) {
            long x2 = x*x;
            
            long maxR1 = (long) Math.ceil(Math.sqrt(r12 - x2));
            long maxR2 = (long) Math.floor(Math.sqrt(r22 - x2));
            answer += maxR2 - maxR1 + 1;
        }
        
        for (long x=r1; x<r2; x++) {
            long x2 = x*x;
            long maxR2 = (long) Math.floor(Math.sqrt(r22 - x2));
            answer += maxR2;
        }
        
        
        return answer * 4;
    }
}