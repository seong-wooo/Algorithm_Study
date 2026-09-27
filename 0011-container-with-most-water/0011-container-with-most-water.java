class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int answer = 0;
        
        while (left < right) {
            answer = Math.max(answer, water(height, left, right));

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return answer;
    }

    private int water(int[] height, int left, int right) {
        return Math.min(height[left], height[right]) * (right - left);
    }
}