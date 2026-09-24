class Solution {
    public int orangesRotting(int[][] grid) {
        
        int answer = 0;
        int[] dy = new int[]{0,0,1,-1};
        int[] dx = new int[]{1,-1,0,0};
        Queue<int[]> q = new LinkedList<>();
        int orange = 0;

        for(int j = 0; j < grid.length; j++) {
            for (int i = 0; i< grid[j].length; i++) {
                if (grid[j][i] == 2) {
                    q.add(new int[]{j, i, 0});
                }

                if (grid[j][i] == 1) {
                    orange++;
                }
            }
        }

         while (!q.isEmpty()) {
            int[] g = q.poll();
            int y = g[0];
            int x = g[1];
            int time = g[2];
            answer = Math.max(answer, time);

            for (int k = 0; k < 4; k++) {
                int ny = dy[k] + y;
                int nx = dx[k] + x;

                if (0 <= ny && ny < grid.length && 0 <= nx && nx < grid[ny].length && grid[ny][nx] == 1) {
                    grid[ny][nx] = '2';
                    q.add(new int[]{ny,nx,time + 1});
                    orange--;
                }
            }
        }

        return orange == 0 ?  answer : -1;
    }
}