class Solution {
    public int minMoves(int target, int maxDoubles) {
        int result = 0;
        while (target > 1) {
            if (maxDoubles == 0) {
                break;
            }

            if (target % 2 == 1) {
                target--;
            } else { 
                maxDoubles--;
                target /= 2;
            }
            result++;
        }
        return result + target - 1;
    }
}

// 101 -> 100 -> 11 -> 10 -> 1

// 10011 -> 10010 -> 1001 -> 1000 -> 100 -> 11 -> 10 -> 1

// 1010 -> 101 -> 100 -> 10 -> 1
