import java.util.*;

class Solution {
    public int[] solution(long begin, long end) {
        int[] answer = new int[(int) (end - begin) + 1];
        if (begin == 1) {
            for (int i = 1; i < answer.length; i ++) {
                answer[i] = 1;
            }
        } else {
            Arrays.fill(answer, 1);
        }
        
        for (long i = begin; i < end + 1; i++) {
            for (long n = 2; n < (int) Math.min(10000000, (int) Math.sqrt(i) + 1); n++) {
                if (i % n == 0) {
                    answer[(int)(i - begin)] = i / n <= 10000000 ? (int) Math.max(answer[(int)(i - begin)], i / n) : (int) Math.max(answer[(int)(i-begin)], n);
                }
            }
        }
        
        
        return answer;
    }
}