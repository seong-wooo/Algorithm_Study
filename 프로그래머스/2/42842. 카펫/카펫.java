class Solution {
    public int[] solution(int brown, int yellow) {
        for (int i = 1; i < (int) Math.sqrt(yellow) + 1; i++) {
            if (yellow % i == 0 && 2 * (i+yellow / i) + 4 == brown) {
                return new int[]{yellow / i + 2 , i + 2};
            }
        }
        return new int[]{};
    }
}