class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int y = 0;
        int x = matrix[y].length - 1;

        while (y < matrix.length && 0 <= x) {
            if (matrix[y][x] == target) {
                return true;
            }

            if (matrix[y][x] > target) {
                x--;
            } else {
                y++;
            }
        }
        return false;
    }
}