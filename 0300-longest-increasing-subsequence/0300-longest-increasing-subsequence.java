class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        
        for (int num : nums) {
            int index = Arrays.binarySearch(tails, 0, size, num);
            if (index < 0) {
                index = - (index + 1);
            }
            tails[index] = num;
            if (index == size) {
                size++;
            }
        }
        return size;
    }
}