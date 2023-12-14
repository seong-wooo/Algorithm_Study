import java.util.*;
import java.util.stream.*;


class Solution {
    public int solution(int[] picks, String[] minerals) {
        int total = Arrays.stream(picks).sum() * 5;
        
        Map<String, Integer> counts = Map.of("diamond", 25, "iron", 5, "stone", 1);
        
        List<Integer> mineralValues = Arrays.stream(minerals)
            .map(counts::get)
            .limit(total)
            .collect(Collectors.toList());
        
        int[][] mineralValuesArray = new int[(int) Math.ceil(mineralValues.size() / 5.0)][5];
        
        
        for (int i = 0; i < mineralValues.size(); i++) {
            int c = i / 5;
            int l = i % 5;
            mineralValuesArray[c][l] = mineralValues.get(i);
        }
        
        Arrays.sort(mineralValuesArray, Comparator.comparing((int[] a) -> Arrays.stream(a).sum()).reversed());
        
        double[] damage = new double[]{25.0, 5.0, 1.0}; 
        int answer = 0;
        for (int[] values : mineralValuesArray) {
            for (int i = 0; i < 3; i++) {
                if (picks[i] > 0) {
                    picks[i] -= 1;
                    double d = damage[i];
                    answer += Arrays.stream(values).map(value -> (int) Math.ceil(value / d)).sum();
                    break;
                }
            }
        }
        
            
        return answer;
    }
}