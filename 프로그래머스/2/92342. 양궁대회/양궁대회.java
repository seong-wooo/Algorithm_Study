import java.util.*; 

class Solution {
    public int[] solution(int n, int[] info) {
        Result result = shoot(n, info, new int[info.length], 0);
        return result.shoot;
    }
    
    public Result shoot(int n, int[] apeach, int[] lion, int index) {
        Result result = new Result(-1, new int[]{-1});
        if (n == 0 || apeach.length == index) {
            lion[lion.length - 1] = n;
            int a = 0, l = 0;
            for (int i = 0; i < apeach.length; i++) {
                if (lion[i] > apeach[i]) {
                    l += 10 - i;
                } else if (apeach[i] != 0) {
                    a += 10 - i;
                }
            }
           if (l > a) {
                return new Result(l - a, Arrays.copyOf(lion, lion.length));
            }
            return result;
        }
        
        if (n > apeach[index]) {
            lion[index] = apeach[index] + 1;
            Result newResult = shoot(n - apeach[index] - 1, apeach, lion, index + 1);
            lion[index] = 0;
            if (newResult.isBiggerThan(result)) {
                result = newResult;
            }
        }
        Result newResult = shoot(n, apeach, lion, index + 1);
        if (newResult.isBiggerThan(result)) {
            return newResult;
        }
        return result;
    }
    
    static class Result {
        int score;
        int[] shoot;
        
        public Result(int score, int[] shoot) {
            this.score = score;
            this.shoot = shoot;
        }
        
        public boolean isBiggerThan(Result o) {
            if (this.score > o.score) {
                return true;
            } 
            else if (this.score < o.score) {
                return false;
            }
            for (int i = this.shoot.length - 1; i >= 0; i--) {
                if (this.shoot[i] == o.shoot[i]) {
                    continue;
                }
                return this.shoot[i] > o.shoot[i];
            }
            return false;
        }
    }
}