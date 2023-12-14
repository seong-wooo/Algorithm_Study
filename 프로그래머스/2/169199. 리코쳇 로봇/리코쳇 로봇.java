import java.util.*;

class Solution {
    public int solution(String[] board) {
        int[] r = new int[2];
        
        for (int j = 0; j < board.length; j++) {
            for (int i = 0; i < board[0].length(); i++) {
                if (board[j].charAt(i) == 'R') {
                    r = new int[]{j, i};
                }
            }
        }
        
        Deque<Robot> q = new LinkedList<>();
        q.add(new Robot(r[0], r[1], 0));
        
        int[] dy = {0,0,1,-1};
        int[] dx = {1,-1,0,0};
        boolean[][] visited = new boolean[board.length][board[0].length()];
        
        while (!q.isEmpty()) {
            Robot robot = q.pollFirst();
            int count = robot.count + 1;
            
            for (int i = 0; i < 4; i++) {
                int ny = robot.y;
                int nx = robot.x;
                while(0 <= ny + dy[i] && ny + dy[i] < board.length
                      && 0 <= nx + dx[i] && nx + dx[i] < board[0].length()
                      && board[ny+dy[i]].charAt(nx + dx[i]) != 'D') {
                        ny += dy[i];
                        nx += dx[i];
                    }
                 
                if (board[ny].charAt(nx) == 'G') {
                    return count;
                }
                
                if (!visited[ny][nx]) {
                    visited[ny][nx] = true;
                    q.add(new Robot(ny, nx, count));
                }
            }
        }
        
        return -1;
    }
    
    static class Robot {
        int y;
        int x; 
        int count;
        
        public Robot(int y, int x, int count) {
            this.y = y;
            this.x = x;
            this.count = count;
        }
    }
}