class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int right = Integer.MIN_VALUE;

        for (int w : weights) {
            right = Math.max(right, w);
        }
        int left = right;
        right *= (weights.length - 1) / days + 1;

        while (left < right) {
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
                right = mid;
            }
        }

        return left;
    }
}