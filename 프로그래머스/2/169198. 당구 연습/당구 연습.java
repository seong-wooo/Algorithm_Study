class Solution {
    public int[] solution(int m, int n, int startX, int startY, int[][] balls) {
        int[][] starts = new int[][] {
            {-startX, startY},
            {startX, 2*n -startY},
            {2*m - startX, startY},
            {startX, -startY},
        };
        
        int[] answer = new int[balls.length];
        
        for (int i = 0; i < balls.length; i++) {
            int minimum = 2000000;
            int[] calc = new int[]{0,1,2,3};
            
            if (startX == balls[i][0]) {
                if (startY > balls[i][1]) {
                    calc = new int[]{0,1,2};
                }
                else {
                    calc = new int[]{0,2,3};
                }
            }
            
            if (startY == balls[i][1]) {
                if (startX > balls[i][0]) {
                    calc = new int[]{1,2,3};
                }
                else {
                    calc = new int[]{0,1,3};
                }
            }
            
            for (int c : calc) {
                int s_x = starts[c][0];
                int s_y = starts[c][1];
                
                minimum = (int) Math.min(minimum, Math.pow(s_x - balls[i][0], 2) + Math.pow(s_y - balls[i][1], 2)); 
            }
            answer[i] = minimum;
        }
        return answer;
    }
}