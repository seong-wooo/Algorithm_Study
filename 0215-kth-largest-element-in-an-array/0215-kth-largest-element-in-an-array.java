class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> pq = new PriorityQueue<>();
        Arrays.sort(nums);
        return nums[nums.length - k];
    }
}