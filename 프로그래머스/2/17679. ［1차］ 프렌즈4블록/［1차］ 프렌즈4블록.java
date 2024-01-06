import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int m, int n, String[] board) {
        char[][] b = new char[board[0].length()][board.length];
        
        for (int j = 0; j < board.length; j++) {
            for (int i = 0; i < board[j].length(); i++) {
                b[i][j] = board[j].charAt(i);
            }
        }
        
        return remove(b);
    }
    
    public int remove(char[][] board) {
        int answer = 0;
        int n = board.length;
        int m = board[0].length;
        boolean[][] toRemove = new boolean[n][m];
        
        for (int j = 0; j < n - 1; j++) {
            for (int i = 0; i < m - 1; i++) {
                if (board[j][i] != '-' && isSquare(board, j, i)) {
                    toRemove[j][i] = true;
                    toRemove[j][i + 1] = true;
                    toRemove[j + 1][i] = true;
                    toRemove[j + 1][i + 1] = true;
                }
            }
        }
        
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                if (toRemove[y][x]) {
                    board[y][x] = '-';
                    answer++;
                }
            }
        }
        
        for (int y = 0; y < n; y++) {
            int idx = m - 1;
            char[] row = new char[m];
            for (int x = m - 1; x > -1; x--) {
                if (board[y][x] != '-') {
                    row[idx--] = board[y][x];
                }
            }
            Arrays.fill(row, 0, idx + 1, '-');
            board[y] = row;       
        }
        
        return answer == 0 ? 0 : answer + remove(board);
        
    }
    
    public boolean isSquare(char[][] board, int y, int x) {
        int[] dy = new int[]{0,1,1};
        int[] dx = new int[]{1,1,0};
        
        char target = board[y][x];
        
        if (target == '-') {
            return false;
        }
        
        for (int i = 0; i < 3; i++) {
            if (target != board[y + dy[i]][x + dx[i]]) {
                return false;
            }
        }
        return true;
    }
}