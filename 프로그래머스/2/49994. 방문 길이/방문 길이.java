import java.util.*;

class Solution {
    public int solution(String dirs) {
        Map<Character, int[]> d = Map.of('U', new int[]{1,0}, 
                                    'L', new int[]{0,-1},
                                    'R', new int[]{0,1},
                                    'D', new int[]{-1,0});
        
        int y = 5;
        int x = 5;
        Set<List<Integer>> visited = new HashSet<>();
        
        for (char dir : dirs.toCharArray()) {
            int[] dydx = d.get(dir);
            int ny = dydx[0] + y;
            int nx = dydx[1] + x;
            
            if (0 <= ny && ny < 11
               && 0 <= nx && nx < 11) {
                visited.add(List.of(y, x, ny, nx));
                visited.add(List.of(ny, nx, y, x));
                y = ny;
                x = nx;
            }   
        }
        return visited.size() / 2;
    }
}