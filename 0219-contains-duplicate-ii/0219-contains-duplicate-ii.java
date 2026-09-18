class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> indexes = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (indexes.containsKey(nums[i]) && i - indexes.get(nums[i]) <= k) {
                return true;
            }

            indexes.put(nums[i], i);
        }

        return false;
    }
}