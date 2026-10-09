class Solution {
    public boolean isValidSudoku(char[][] board) {
        // rows
        for (int j = 0; j < board.length; j++) {
            int[] counter = new int[10];
            for (int i = 0; i < board[j].length; i++) {
                if(board[j][i] == '.') {
                    continue;
                }
                counter[board[j][i] - '0']++;
                if (counter[board[j][i] - '0'] == 2) {
                    return false;
                }
            }
        }

        // cols
        for (int i = 0; i < board[0].length; i++) {
            int[] counter = new int[10];
            for (int j = 0; j < board.length; j++) {
                if(board[j][i] == '.') {
                    continue;
                }
                counter[board[j][i] - '0']++;
                if (counter[board[j][i] - '0'] == 2) {
                    return false;
                }
            }
        }


        // 격자
        for (int y = 0; y < 9; y += 3) {
            for (int x = 0; x < 9; x += 3) {
                int[] counter = new int[10];
                for (int j = y; j < y + 3; j++) {
                    for (int i = x; i < x + 3; i++) {
                        if(board[j][i] == '.') {
                           continue;
                        }   
                        counter[board[j][i] - '0']++;
                        if (counter[board[j][i] - '0'] == 2) {
                            return false;
                        }
                    }
                }
            }
        }

        return true;
    }
}