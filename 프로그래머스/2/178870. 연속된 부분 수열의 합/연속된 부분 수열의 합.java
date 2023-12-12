class Solution {
    public int[] solution(int[] sequence, int k) {
        int left = 0;
        int right = 0;
        int current = sequence[left];
        int currentMinLength = Integer.MAX_VALUE;
        int[] result = new int[2];
        
        while (left <= right && right < sequence.length) {
            
            if (current == k) {
                if (right - left < currentMinLength) {
                    currentMinLength = right - left;
                    result = new int[]{left, right};
                }
                current -= sequence[left];
                left++;
                right++;
                if (right < sequence.length) {
                    current += sequence[right];
                }
            } else if (current > k) {
                current -= sequence[left];
                left++;
            } else {
                right++;
                if (right < sequence.length) {
                    current += sequence[right];
                }
            }
        }
        
        return result;
    }
}