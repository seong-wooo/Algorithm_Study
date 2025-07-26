class Solution {
    public int largestAltitude(int[] gain) {
        int answer = 0;
        int current = 0;
        for(int g : gain) {
            current += g;
            answer = Math.max(answer, current);
        }
        return answer;
    }
}