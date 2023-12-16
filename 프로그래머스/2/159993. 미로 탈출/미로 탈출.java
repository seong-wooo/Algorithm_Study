import java.util.*;

class Solution {
    public int solution(String[] maps) {
        
        int[] start = new int[2];
        int[] lebber = new int[2];
        int[] exit= new int[2];
        
        for (int j = 0; j < maps.length; j++) {
            for (int i = 0; i < maps[0].length(); i++) {
                if (maps[j].charAt(i) == 'S') {
                    start = new int[]{j, i};
                } else if (maps[j].charAt(i) == 'L') {
                    lebber = new int[]{j, i};
                } else if (maps[j].charAt(i) == 'E') {
                    exit = new int[]{j, i};
                }
            }
        }

        
        int first = bfs(start, lebber, maps);

        if (first == -1) {
            return -1;
        }
        
        int second = bfs(lebber, exit, maps);
        
        if (second == -1) {
            return -1;
        }
        
        return first + second;
    }
    
    public int bfs(int[] start, int[] end, String[] maps) {
        Deque<Location> q = new LinkedList<>();
        q.add(new Location(start[0], start[1], 0));
        
        boolean[][] visited = new boolean[maps.length][maps[0].length()];
        visited[start[0]][start[1]] = true;
        
        int[] dy = new int[]{0,0,1,-1};
        int[] dx = new int[]{1,-1,0,0};
        
        while (!q.isEmpty()) {
            Location l = q.pollFirst();
            int y = l.y;
            int x = l.x;
            int count = l.count;
            System.out.println(Arrays.toString(new int[]{y, x, count}));
            count++;
            
            for (int i=0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                
                if (ny == end[0] && nx == end[1]) {
                    return count;
                }
                
                if (
                    (0 <= ny && ny < maps.length)
                    && (0 <= nx && nx < maps[0].length())
                    && !visited[ny][nx]
                    && maps[ny].charAt(nx) != 'X'
                ) { 
                    visited[ny][nx] = true;
                    q.add(new Location(ny, nx, count));
                }
            }
            
            
        }
        
        return -1;
    }
    
    public class Location {
        int y;
        int x;
        int count;
        
        public Location(int y, int x, int count) {
            this.y = y;
            this.x = x;
            this.count = count;
        }
    }
    
}