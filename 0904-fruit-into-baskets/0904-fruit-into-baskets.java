class Solution {
    public int totalFruit(int[] fruits) {
        int last = -1, secondLast = -1;
        int lastRun = 0; 
        int current = 0;
        int answer = 0;

        for (int f : fruits) {
            if (last == f) {
                current++;
                lastRun++;
            } else if (secondLast == f) {
                current++;
                lastRun = 1;
                secondLast = last;
                last = f;
            } else {
                current = lastRun + 1;
                lastRun = 1;
                secondLast = last;
                last = f;
            }

            answer = Math.max(answer, current);
        }
        return answer;
    }
}