class Solution {
    int solution(int[][] land) {
        for (int j = land.length - 2; j > -1; j--) {
            for (int i = 0; i < land[j].length; i++) {
                int max = 0;
                for (int k = 0; k < i; k++) {
                    max = (int) Math.max(max, land[j+1][k]);
                }
                
                for (int k = i + 1; k < land[j].length; k++) {
                    max = (int) Math.max(max, land[j+1][k]);
                }
                land[j][i] += max;
            }
        }
        
        int answer = 0;
        for (int l : land[0]) {
            if (answer < l) {
                answer = l;
            }
        }
        
        return answer;
    }
}