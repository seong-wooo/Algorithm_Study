import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<int[]> answer = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            answer.add(new int[i]);
        }
        
        int[] dy = new int[]{1, 0, -1};
        int[] dx = new int[]{0, 1, -1};
        
        int node = 1;
        int y = 0, x = 0, count = 0;
        
        while (count < n) {
            for (int i = 0; i < n - count; i++) {
                answer.get(y)[x] = node;
                node++;
                if (i != n - count - 1) {
                    y += dy[count % 3];
                    x += dx[count % 3];
                }
            }
            count++;
            y += dy[count % 3];
            x += dx[count % 3];
        }
        
        int[] result = new int[n * (n + 1) / 2];
        
        int j = 0;
        for (int[] a : answer) {
            for(int b : a) {
                result[j] = b;
                j++;
            }
        }
        
        
        
        return result;
    }
}