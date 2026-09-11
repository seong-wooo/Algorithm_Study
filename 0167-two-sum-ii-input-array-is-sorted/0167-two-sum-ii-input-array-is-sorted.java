class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        for (int i = 0; i < numbers.length; i++) {
            int current = numbers[i];

            int idx = Arrays.binarySearch(numbers, i + 1, numbers.length, target - current);
            if (idx >= 0) {
                return new int[]{i + 1, idx + 1};
            }
        }

        return new int[]{-1, -1};
    }
}