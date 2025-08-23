class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0; i < numbers.length - 1; i++) {
            int t = target - numbers[i];

            int left = i + 1;
            int right = numbers.length - 1;

            while (left <= right) {
                int mid = left + (right - left) / 2;

                if (numbers[mid] > t) {
                    right = mid - 1;
                } else if (numbers[mid] == t) {
                    return new int[] {i + 1, mid + 1};
                } else {
                    left = mid + 1;
                }
            }
        }
        return null;
    }
}