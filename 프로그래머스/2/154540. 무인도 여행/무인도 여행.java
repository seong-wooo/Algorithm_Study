import java.util.*;

class Solution {
    public int[] solution(String[] maps) {
        boolean[][] visited = new boolean[maps.length][maps[0].length()];
        Queue<int[]> q = new LinkedList<>();
        List<Integer> answer = new ArrayList<>();
        int[] dy = new int[]{1,-1,0,0};
        int[] dx = new int[]{0,0,1,-1};
        for (int j = 0; j < maps.length; j++) {
            for (int i = 0; i < maps[0].length(); i++) {
                if (maps[j].charAt(i) != 'X' && !visited[j][i]) {
                    visited[j][i] = true;
                    int days = Character.getNumericValue(maps[j].charAt(i));
                    q.add(new int[]{j, i});
                    
                    while (!q.isEmpty()) {
                        int[] yx = q.poll();
                        int y = yx[0];
                        int x = yx[1];
                        
                        for (int k = 0; k < 4; k++) {
                            int ny = y + dy[k];
                            int nx = x + dx[k];
                            
                            if (0 <= ny && ny < maps.length && 0 <= nx && nx < maps[0].length() && !visited[ny][nx] && maps[ny].charAt(nx) != 'X') {
                                days += Character.getNumericValue(maps[ny].charAt(nx));
                                visited[ny][nx] = true;
                                q.add(new int[]{ny, nx});
                            }
                        }
                    }
                    answer.add(days);
                }
            }
        }
        
        return answer.isEmpty() ? new int[]{-1} : answer.stream().mapToInt(x -> x).sorted().toArray();
    }
}