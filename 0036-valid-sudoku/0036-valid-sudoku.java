class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] boxes = new int[9];

        for (int y = 0; y < 9; y++) {
            for(int x = 0; x <9; x++) {
                if (board[y][x] == '.') {
                    continue;
                }

                int bit = 1 << board[y][x] - '0';
                int b = (y / 3) * 3 + x / 3;

                if ((rows[y] & bit) != 0 || (cols[x] & bit) != 0 || (boxes[b] & bit) != 0) {
                    return false;
                } 

                rows[y] |= bit;
                cols[x] |= bit;
                boxes[b] |= bit;
            }
        }
        return true;
    }
}