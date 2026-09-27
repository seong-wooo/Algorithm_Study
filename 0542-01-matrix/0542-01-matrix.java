class Solution {
    private final int[] dy = new int[]{0,0,1,-1};
    private final int[] dx = new int[]{1,-1,0,0};

    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int[][] answer = new int[rows][cols];

        Queue<int[]> q = new ArrayDeque<>();

        for(int y = 0; y < rows; y++) {
            for (int x = 0; x < cols; x++) {
                if (mat[y][x] == 0) {
                    q.add(new int[]{y,x});
                } else {
                    answer[y][x] = -1;
                }
            }
        }

        while (!q.isEmpty()) {
            int[] yx = q.poll();   
            int y = yx[0];
            int x = yx[1];

            for(int k = 0; k < 4; k++) {
                int ny = y + dy[k];
                int nx = x + dx[k];

                if (0 <= ny && ny < rows && 0<= nx && nx <cols && answer[ny][nx] < 0) {
                    answer[ny][nx] = answer[y][x] + 1;
                    q.add(new int[]{ny, nx});
                }
            }
        }

        return answer;
    }
}