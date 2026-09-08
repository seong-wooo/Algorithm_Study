class Solution {
    public int numIslands(char[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int[] dx = new int[]{1,-1,0,0};
        int[] dy = new int[]{0,0,1,-1};

        int answer = 0;
        for (int j = 0; j < grid.length; j++) {
            for (int i = 0; i < grid[j].length; i++) {
                if (grid[j][i] == '1') {
                    answer++;
                    q.offer(new int[]{j, i});
                    grid[j][i] = '0';

                    while(!q.isEmpty()) {
                        int[] yx = q.poll();
                        int y = yx[0];
                        int x = yx[1];

                        for (int k = 0; k < 4; k++) {
                            int ny = y + dy[k];
                            int nx = x + dx[k];

                            if (0 <= ny && ny < grid.length && 0 <= nx && nx < grid[ny].length && grid[ny][nx] == '1') {
                                grid[ny][nx] = '0';
                                q.offer(new int[]{ny, nx});
                            }
                        }   
                    }
                }
            }
        }

        return answer;
    }
}