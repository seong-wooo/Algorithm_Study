class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int[] dy = new int[]{0,0,1,-1};
        int[] dx = new int[]{1,-1,0,0};
        int answer = 0;
        Queue<int[]> q = new ArrayDeque<>();

        for (int j = 0; j < grid.length; j++) {
            for (int i = 0; i < grid[j].length; i++) {
                if(grid[j][i] == 1) {
                    grid[j][i] = 0;
                    int size = 1;
                    q.add(new int[]{j, i});

                    while (!q.isEmpty()) {
                        int[] yx = q.poll();
                        int y = yx[0];
                        int x = yx[1];

                        for (int k = 0; k < 4; k++) {
                            int ny = y + dy[k];
                            int nx = x + dx[k];

                            if (0 <= ny && ny < grid.length && 0 <= nx && nx < grid[j].length && grid[ny][nx] == 1) {
                                grid[ny][nx] = 0;
                                size++;
                                q.add(new int[]{ny, nx});
                            }
                        }
                    }
                    answer = Math.max(answer, size);
                }
            }
        }
        return answer;
    }
}