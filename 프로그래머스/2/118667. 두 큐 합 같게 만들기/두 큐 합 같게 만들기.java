import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        long t1 = Arrays.stream(queue1).mapToLong(x -> x).sum();
        long t2 = Arrays.stream(queue2).mapToLong(x -> x).sum();
        long total = t1 + t2;
        
        if (total % 2 != 0) {
            return -1;
        }
        
        long target = total / 2;
        
        
        int[] q = new int[queue1.length + queue2.length];
        
        for (int i = 0; i < queue1.length; i++) {
            q[i] = queue1[i];
            q[i + queue1.length] = queue2[i];
        }
        
        int start = 0;
        int end = queue1.length - 1;
        int result = 0;
        
        while (t1 != target) {
            if (t1 > target) {
                t1 -= q[start];
                start++;
            } else {
                end += 1;
                if (end == q.length) {
                    return -1;
                }
                t1 += q[end];
            }
            result++;
        }
        return result;
    }
}