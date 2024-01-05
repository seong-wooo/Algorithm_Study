import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int[] dy = new int[]{0,0,1,-1};
        int[] dx = new int[]{1,-1,0,0};
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0,0,1});
        maps[0][0] = 1;
        
        while(!q.isEmpty()) {
            int[] yXCount = q.poll();
            
            for (int i = 0; i < 4; i++) {
                int ny = yXCount[0] + dy[i]; 
                int nx = yXCount[1] + dx[i]; 
                
                if (ny == maps.length - 1 && nx == maps[0].length - 1) {
                    return yXCount[2] + 1;
                }
                
                if (0 <= ny && ny < maps.length && 0 <= nx && nx < maps[0].length && maps[ny][nx] == 1) {
                    maps[ny][nx] = 0;
                    q.add(new int[]{ny, nx, yXCount[2] + 1});
                }
            }
        }
        
        return -1;
    }
}