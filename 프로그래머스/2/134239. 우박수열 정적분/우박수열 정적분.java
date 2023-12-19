import java.util.*;

class Solution {
    public double[] solution(int k, int[][] ranges) {
        List<Integer> a = new ArrayList<>();
        a.add(k);
        
        while (k > 1) {
            k = k % 2 == 0 ? k / 2 : 3 * k + 1;
            a.add(k);
        }
        
        double[] area = new double[a.size()];
        for (int i = 0; i< a.size() - 1; i++) {
            area[i + 1] = area[i] + (a.get(i) + a.get(i + 1)) / 2.0;
        }
        
        int n = area.length - 1;
        double[] answer = new double[ranges.length];
        
        for (int i = 0; i < ranges.length; i++) {
            int[] r = ranges[i];
            int left = r[0];
            int right = n + r[1];
            
            if (left > right) {
                answer[i] = -1;
                continue;
            }
            
            answer[i] = area[right] - area [left];
        }
        return answer;
    }
}