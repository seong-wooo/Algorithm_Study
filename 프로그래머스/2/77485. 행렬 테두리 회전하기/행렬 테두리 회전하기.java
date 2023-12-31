import java.util.*;

class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[][] rc = new int[rows][columns];
        int[] answer = new int[queries.length];
        
        for (int j = 0; j < rows; j++) {
            for (int i = 0; i < columns; i++) {
                rc[j][i] = j * columns + i + 1;
            }
        }
        
        for (int k = 0; k < queries.length; k++) {
            int[] q = queries[k];
            int y1 = q[0] - 1;
            int x1 = q[1] - 1;
            int y2 = q[2] - 1;
            int x2 = q[3] - 1;
            
            List<Integer> change = new ArrayList<>();
            int temp = rc[y1][x1];
            change.add(temp);
            
            for (int x = x1; x < x2; x++) {
                int temp2 = temp;
                temp = rc[y1][x+1];
                rc[y1][x+1] = temp2;
                change.add(temp);
            }
            
            for (int y = y1; y < y2; y++) {
                int temp2 = temp;
                temp = rc[y+1][x2];
                rc[y+1][x2] = temp2;
                change.add(temp);
            }
            
            for (int x = x2; x > x1; x--) {
                int temp2 = temp;
                temp = rc[y2][x-1];
                rc[y2][x-1] = temp2;
                change.add(temp);
            }
            
            for (int y = y2; y > y1; y--) {
                int temp2 = temp;
                temp = rc[y-1][x1];
                rc[y-1][x1] = temp2;
                change.add(temp);
            }
            
            answer[k] = Collections.min(change);
            
        }
        
        return answer;
    }
}