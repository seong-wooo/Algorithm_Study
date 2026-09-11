class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int y = 0;
        int x = matrix[0].length - 1;

        while(y < matrix.length && 0 <= x && matrix[y][x] != target) {
            if (matrix[y][x] > target) {
                x--;
            } else {
                y++;
            }
        }
        return y < matrix.length && 0 <= x && matrix[y][x] == target;
    }
}