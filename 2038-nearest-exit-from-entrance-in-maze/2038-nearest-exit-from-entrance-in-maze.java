import java.util.*;

class Solution {
    int[] dy = {0, 0, 1, -1};
    int[] dx = {1, -1, 0, 0};

    public int nearestExit(char[][] maze, int[] entrance) {
        int n = maze.length;
        int m = maze[0].length;

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{entrance[0], entrance[1], 0}); // y, x, steps
        maze[entrance[0]][entrance[1]] = '+'; // 시작점 방문 처리

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int y = cur[0];
            int x = cur[1];
            int steps = cur[2];

            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                if (maze[ny][nx] == '+') continue; // 벽 또는 방문한 곳

                // 출구 조건: 경계에 있고 entrance가 아닌 경우
                if (ny == 0 || ny == n - 1 || nx == 0 || nx == m - 1) {
                    return steps + 1;
                }

                maze[ny][nx] = '+'; // 방문 처리
                q.add(new int[]{ny, nx, steps + 1});
            }
        }

        return -1; // 출구를 못 찾음
    }
}
