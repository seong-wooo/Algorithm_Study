class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> indexes = new HashMap<>(nums.length);

        for (int i = 0; i < nums.length; i++) {
            if (i - indexes.getOrDefault(nums[i], -k-1) <= k) {
                return true;
            }

            indexes.put(nums[i], i);
        }

        return false;
    }
}