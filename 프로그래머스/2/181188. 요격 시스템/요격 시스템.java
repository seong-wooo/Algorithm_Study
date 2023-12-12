import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        Arrays.sort(targets, Comparator.comparingInt((int[] a) -> a[0]).thenComparingInt(a -> a[1]));   
        List<Shoot> answer = new ArrayList<>();
        answer.add(new Shoot(targets[0][0], targets[0][1]));
        
        for (int i = 1; i < targets.length; i++) {
            Shoot lastShoot = answer.get(answer.size() - 1);
            if (lastShoot.end > targets[i][0]) {
                lastShoot.change(targets[i][0], Math.min(lastShoot.end, targets[i][1]));
            } else {
                answer.add(new Shoot(targets[i][0], targets[i][1]));
            }
        }
        
        
        return answer.size();
    }
    
    static class Shoot {
        int start; 
        int end;
        
        public Shoot(int start, int end) {
            this.start = start;
            this.end = end;
        }
        
        public void change(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}