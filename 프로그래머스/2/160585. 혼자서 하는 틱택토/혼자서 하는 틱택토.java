class Solution {
    public int solution(String[] board) {
        int[] ox = countOX(board);
        int[] oxLine = countLine(board);
        
        int o = ox[0];
        int x = ox[1];
        int oL = oxLine[0];
        int xL = oxLine[1];
        
        
        boolean a = oL == 0 && xL == 0;
        boolean b = oL == 1 && xL == 0;
        boolean c = oL == 0 && xL == 1;
        boolean d = oL == 2 && xL == 0;
        
        if (a && (o == x || o == x + 1)) {
            return 1;
        }
        
        if (b && ((o == 3 && x == 2) || (o == 4 && x == 3))) {
            return 1;
        }
        
        if (c && (o == x)) {
            return 1;
        }
        
        if (d && (o == 5 && x == 4)) {
            return 1;
        }
        
        return 0;
        
    }
    
    public int[] countOX(String[] board) {
        int o = 0;
        int x = 0;
        
        for (String b : board) {
            for (char ox : b.toCharArray()) {
                if (ox == 'O') {
                    o++;
                } else if (ox == 'X') {
                    x++;
                }
            }
        }
        return new int[]{o, x};
    }
    
    public int[] countLine(String[] board) {
        int o = 0;
        int x = 0;
        
        int[][] lines = new int[][]{
            {0,1,2}, {3,4,5}, {6,7,8}, {0,3,6}, {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6} 
        };
        
        for (int[] line : lines) {
            if (board[line[0] / 3].charAt(line[0] % 3) == board[line[1] / 3].charAt(line[1] % 3) && board[line[1] / 3].charAt(line[1] % 3) == board[line[2] / 3].charAt(line[2] % 3)) {
                if (board[line[0] / 3].charAt(line[0] % 3) == 'O') {
                    o++;   
                } else if(board[line[0] / 3].charAt(line[0] % 3) == 'X') {
                    x++;
                }
            }
        }
        return new int[]{o,x};
    }
}