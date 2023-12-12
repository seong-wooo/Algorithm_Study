import java.util.*;

class Solution {
    public int solution(int[][] land) {
        Map<Integer, Integer> oils = getOils(land);
        
        int result = 0;
        for (int x = 0; x < land[0].length; x++) {
            Set<Integer> s = new HashSet<>();    
            int xTotal = 0;
            for (int y = 0; y < land.length; y++) {
                if (land[y][x] != 0 && !s.contains(land[y][x])) {
                    s.add(land[y][x]);
                    xTotal += oils.get(land[y][x]);
                }
            }
            result = Math.max(result, xTotal);
        }
        return result;
    }
    
    public Map<Integer, Integer> getOils(int[][] land) {
        int n = land.length;
        int m = land[0].length;
        
        int group = 2;
        Map<Integer, Integer> oils = new HashMap<>();
        
        int[] dy = new int[]{0,0,1,-1};
        int[] dx = new int[]{1,-1,0,0};
        
        
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                if (land[y][x] == 1) {
                    Queue<int[]> q = new LinkedList<>();       
                    group++;
                    land[y][x] = group;
                    q.add(new int[]{y, x});
                    
                    while (!q.isEmpty()) {
                        int[] yx = q.poll();
                        int j = yx[0];
                        int i = yx[1];
                        
                        oils.merge(group, 1, (o, v) -> o + 1);
                        
                        for (int k = 0; k < 4; k++) {
                            int ny = j + dy[k];
                            int nx = i + dx[k];
                            
                            if (0 <= ny && ny < n && 0 <= nx && nx < m && land[ny][nx] == 1) {
                                land[ny][nx] = group;
                                q.add(new int[]{ny, nx});
                            }
                        }
                    }
                }
            }
        }
        
        return oils;
    }
}