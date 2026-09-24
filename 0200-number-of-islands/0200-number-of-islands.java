class Solution {
    public int numIslands(char[][] grid) {
        Queue<int[]> q = new ArrayDeque<>();
        int answer = 0;
        int[] dy = new int[]{0,0,1,-1};
        int[] dx = new int[]{1,-1,0,0};

        for (int j = 0; j < grid.length; j++) {
            for (int i = 0; i < grid[j].length; i++) {
                if (grid[j][i] == '1') {
                    q.add(new int[]{j, i});
                    grid[j][i] = '0';
                    answer++;

                    while (!q.isEmpty()) {
                        int[] g = q.poll();
                        int y = g[0];
                        int x = g[1];

                        grid[y][x] = '0';

                        for (int k = 0; k < 4; k++) {
                            int ny = dy[k] + y;
                            int nx = dx[k] + x;

                            if (0 <= ny && ny < grid.length && 0 <= nx && nx < grid[ny].length && grid[ny][nx] == '1') {
                                q.add(new int[]{ny, nx});
                                grid[ny][nx] = '0';
                            }
                        }
                    }
                }
            }
        }
        return answer;
    }
}