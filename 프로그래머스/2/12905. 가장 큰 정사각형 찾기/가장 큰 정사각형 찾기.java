import java.util.*;

class Solution
{
    public int solution(int [][]board)
    {
        double answer = 0;
        int[][] dp = new int[board.length+1][board[0].length + 1];
        
        for (int y = 0; y < board.length; y++) {
            for (int x = 0; x < board[0].length; x++) {
                dp[y+1][x+1] = board[y][x] == 0 ? 0 : 1 + (int) Math.min(Math.min(dp[y][x], dp[y+1][x]), dp[y][x+1]);
                answer = Math.max(answer, dp[y+1][x+1]);
            }
        }
        
        return (int) (answer * answer);
    }
}