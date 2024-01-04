class Solution {
    public int solution(int n) {
        int[] nums = new int[n/2 + 2];
        for (int i = 1; i < n/2 + 2; i++) {
            nums[i] = i * (i + 1) / 2;
        }
        int answer = 0;
        
        for(int right = 1; right < n/2 + 2; right++) {
            int left = right - 1;
            while(left > 0 && nums[right] - nums[left] < n) {
                left--;
            }
            
            if (nums[right] - nums[left] == n) {
                answer++;
            }
        }
        
        return n > 2 ? answer + 1 : answer;
    }
}