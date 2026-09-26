class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int right = Integer.MIN_VALUE;

        for (int w : weights) {
            right = Math.max(right, w);
        }
        int left = right;
        right *= Math.ceil((double) weights.length / days);

        int answer = Integer.MAX_VALUE;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int currentDays = 0;

            int sum = 0;
            for (int w :weights) {
                if (sum + w <= mid) {
                    sum += w;
                } else {
                    sum = w;
                    currentDays++;
                    if (currentDays > days) {
                        break;
                    }
                }
            }
            currentDays++;

            if (currentDays > days) {
                left = mid + 1;
            } else {
                answer = Math.min(answer, mid);
                right = mid - 1;
            }
        }

        return answer;
    }
}