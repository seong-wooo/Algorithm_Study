class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> indexes = new HashMap<>(nums.length);

        for (int i = 0; i < nums.length; i++) {
            Integer prev = indexes.put(nums[i], i);

            if (prev != null && i - prev <= k) {
                return true;
            }
        }

        return false;
    }
}