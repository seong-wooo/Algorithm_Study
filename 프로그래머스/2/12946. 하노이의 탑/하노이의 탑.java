import java.util.*;


class Solution {
    public int[][] solution(int n) {
        List<int[]> answer = new LinkedList<>();
        hanoi(answer, n, 1, 3);
        return answer.toArray(new int[0][]);       
    }
    
    
    public void hanoi(List<int[]> answer, int n, int start, int end) {
        if (n == 0) {
            return;
        }
        
        hanoi(answer, n-1, start, 6-start-end);
        answer.add(new int[]{start, end});
        hanoi(answer, n-1, 6-start-end, end);
    }
}