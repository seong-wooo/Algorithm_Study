class Solution {
    public int totalFruit(int[] fruits) {
        int last = -1, secondLast = -1;
        int lastRun = 0;   // 마지막 종류가 끝에서 연속으로 나온 길이
        int current = 0;   // 현재 유효한 윈도우 길이
        int answer = 0;

        for (int f : fruits) {
            if (f == last || f == secondLast) {
                current++;
            } else {
                current = lastRun + 1;
            }

            if (f == last) {
                lastRun++;
            } else {
                lastRun = 1;
                secondLast = last;
                last = f;
            }

            answer = Math.max(answer, current);
        }
        return answer;
    }
}