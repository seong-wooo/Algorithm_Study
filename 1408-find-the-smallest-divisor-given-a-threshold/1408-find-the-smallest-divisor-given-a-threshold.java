class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int right = (int) Math.pow(10, 6);
        int left = 1;     
        int answer = right;

        while (left <= right) {
            int mid = (left + right) / 2;
            int result = sum(nums, mid);

            if (result > threshold) {
                left = mid + 1;
            } 
            
            else {
                answer = (int) Math.min(answer, mid);
                right = mid - 1;
            }
        }

        return answer;
    }

    public int sum(int[] nums, int mid) {
        int result = 0;

        for (int num : nums) {
            result += (int) Math.ceil((double) num /mid);
        }
        return result;
    }
}