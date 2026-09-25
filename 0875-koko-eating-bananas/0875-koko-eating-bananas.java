class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
        int left = 0; 
        int right = Integer.MAX_VALUE;
        int answer = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            int time = 0;

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