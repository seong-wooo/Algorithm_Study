class Solution {
    public int splitArray(int[] nums, int k) {
        // 최소 합을 기준으로 이분탐색

        long total = 0;

        long[] 누적합 = new long[nums.length + 1];
        
        for (int i = 1; i < nums.length + 1; i++) {
            누적합[i] = 누적합[i-1] + nums[i-1];
            total += nums[i-1];
        }

        long left = 0;
        long right = total;
        long answer = 0;
        while (left <= right) {
            long mid = (left + right) / 2;

            if(k개_이하로_나눌_수_있나(누적합, k, mid)) {
                right = mid - 1;
                answer = mid;
            } else {
                left = mid + 1;
            }
        }

        return (int) answer;
    }

    public boolean k개_이하로_나눌_수_있나(long[] 누적합, int k, long target) {
        int left = 0;
        int result = 0;

        for (int right = 1; right < 누적합.length; right++) {
            if (누적합[right] - 누적합[right-1] > target) {
                return false;
            }

            if(누적합[right] - 누적합[left] > target) {
                left = right - 1;
                result++;
            }
        }

        return result + 1 <= k;
    }
}