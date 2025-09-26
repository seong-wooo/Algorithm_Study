class Solution {
    public int findKthLargest(int[] nums, int k) {
        int[] negative = new int[(int) Math.pow(10, 4) + 1];
        int[] positive = new int[(int) Math.pow(10, 4) + 1];
        
        for (int num : nums) {
            if (num < 0) {
                negative[-num]++;
            } else { 
                positive[num]++;
            }
        }
        
        int count = nums.length - k + 1;

        for(int i = negative.length - 1; i > 0; i--) {
            count -= negative[i];
            if (count <= 0) {
                return -i;
            }
        }

        for (int i = 0; i < positive.length; i++) {
            count -= positive[i];

            if (count <= 0) {
                return i;
            }
        }

        return Integer.MAX_VALUE;
    }
}