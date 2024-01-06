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
        Set<List<Integer>> delete = new HashSet<>();
        int n = board.length;
        int m = board[0].length;
        
        for (int j = 0; j < n - 1; j++) {
            for (int i = 0; i < m - 1; i++) {
                if (board[j][i] != '-' && isSquare(board, j, i)) {
                    delete.add(List.of(j, i));
                    delete.add(List.of(j, i + 1));
                    delete.add(List.of(j + 1, i));
                    delete.add(List.of(j + 1, i + 1));
                }
            }
        }
        
        if (delete.isEmpty()) {
            return answer;
        }
        answer += delete.size();
        
        for (List<Integer> yx : delete) {
            board[yx.get(0)][yx.get(1)] = '-';
        }
        
        
        for (int y = 0; y < board.length; y++) {
            char[] b = board[y];
            StringBuilder sb = new StringBuilder();
            
            for (char c : b) {
                sb.append(c);    
            }
            
            String s = Arrays.stream(sb.toString()
                          .split("-"))
                .collect(Collectors.joining());
            
            s = "-".repeat(m - s.length()) + s;
            
            for (int i = 0; i < m; i++) {
                board[y][i] = s.charAt(i);
            }                        
        }
        return answer + remove(board);
        
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