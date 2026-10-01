class Solution {
    public int search(int[] nums, int target) {
        int answer = Arrays.binarySearch(nums, target);

        return answer >= 0 ? answer : -1;
    }
}