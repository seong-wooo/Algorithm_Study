class Solution {
    int[] answer = {0, 0};
    
    public int[] solution(int[][] arr) {
        press(arr, 0, 0, arr.length);
        return answer;
    }
    
    public void press(int[][] arr, int y, int x, int l) {
        if (isAllSame(arr, y, x, l)) {
            answer[arr[y][x]]++;
            return;
        }
        
        press(arr, y, x, l / 2);
        press(arr, y + l / 2, x, l / 2);
        press(arr, y, x + l / 2, l / 2);
        press(arr, y + l / 2, x + l / 2, l / 2);
    }
    
    
    public boolean isAllSame(int[][] arr, int y, int x, int l) {
        int target = arr[y][x];
        
        for (int j = y; j < y + l; j++) {
            for (int i = x; i < x + l; i++) {
                if (target != arr[j][i]) {
                    return false;
                }
            }
        }
        return true;
    }
}