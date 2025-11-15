class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid[0][0] == 1) {
            return 0;
        }

        int[][] graph = new int[obstacleGrid.length][obstacleGrid[0].length];
        boolean[][] qp = new boolean[obstacleGrid.length][obstacleGrid[0].length];
        Queue<int[]> q = new ArrayDeque<>();

        graph[0][0] = 1;
        qp[0][0] = true;

        q.add(new int[]{0,0});
        
        int[] dy = new int[]{0,1};
        int[] dx = new int[]{1,0};

        while (!q.isEmpty()) {
            int[] point = q.poll();
            int y = point[0];
            int x = point[1];

            for (int i = 0; i < 2; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (0 <= ny && ny < graph.length && 0 <= nx && nx < graph[0].length && obstacleGrid[ny][nx] == 0) {
                    graph[ny][nx] += graph[y][x];
                    if (!qp[ny][nx]) {
                        qp[ny][nx] = true;
                        q.add(new int[]{ny,nx});
                    }
                }
            }
        }

        return graph[graph.length-1][graph[0].length - 1];
    }
}