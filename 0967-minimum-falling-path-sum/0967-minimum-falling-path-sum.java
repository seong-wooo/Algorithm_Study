class Solution {
    public int minFallingPathSum(int[][] matrix) {
        for (int j = 1; j < matrix.length; j++) {
            for (int i = 0; i < matrix[j].length; i++) {
                matrix[j][i] += findMin(i, matrix[j-1]);
            }
        }

        int answer = Integer.MAX_VALUE;

        for (int i = 0; i < matrix[matrix.length -1].length; i++) {
            answer = Math.min(answer, matrix[matrix.length -1][i]);
        }

        return answer;
    }

    public int findMin(int i, int[] matrix) {
        if (i == 0) {
            return Math.min(matrix[i+1],  matrix[i]);
        }

        if (i == matrix.length - 1) {
            return Math.min(matrix[i - 1],  matrix[i]);
        }

        return Math.min( matrix[i], Math.min(matrix[i+1], matrix[i - 1]));
    }
}