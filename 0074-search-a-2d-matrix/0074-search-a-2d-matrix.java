class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // 1. 세로 행을 기준으로 이진 탐색
        int left = 0;
        int right = matrix.length - 1;
        int row;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if(matrix[mid][0] == target) {
                return true;
            }

            if (matrix[mid][0] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        if (right < 0) {
            return false;
        }
        row = right;
    
        // 2. 가로 행을 기준으로 이진 탐색
        left = 1; 
        right = matrix[row].length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if(matrix[row][mid] == target) {
                return true;
            }

            if (matrix[row][mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}