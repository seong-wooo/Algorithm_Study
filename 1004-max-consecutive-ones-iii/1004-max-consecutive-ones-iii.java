class Solution {
    public int longestOnes(int[] nums, int k) {
        Queue<Integer> zeroIndex = new LinkedList<>();
        int answer = 0;
        int left = 0;
        for (int right = 0; right < nums.length; right++) {
            if(nums[right] == 0) {
                if (k > 0) {
                    zeroIndex.offer(right);
                    k--;
                } else {
                    if (!zeroIndex.isEmpty()) {
                        left = zeroIndex.poll() + 1;
                        zeroIndex.offer(right);
                    } else {
                        left = right + 1;
                    }   
                }
            }
            answer = Math.max(answer, right - left + 1);
        }
        return answer;
    }
}