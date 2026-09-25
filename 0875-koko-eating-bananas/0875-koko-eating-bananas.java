class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
        int left = 1; 
        int right = 0;
        int answer = 0;
        for (int p :piles) {
            right = Math.max(right, p);
        }

        while (left <= right) {
            int mid = left + (right - left) / 2;

            long time = 0;

            for (int p : piles) {
                time += Math.ceil((double) p / mid);
            }

            if (time <= h) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return answer;
    }
}