class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Arrays.sort(players);
        Arrays.sort(trainers);

        int index = - 1;
        int result = 0;

        for (int player: players) {
            index = binarySearch(player, trainers, index + 1);
            if (index == -1) {
                return result;
            }
            result++;
        }
        return result;
    }


    public int binarySearch(int x, int[] nums, int left) {
        int result = -1;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = (right + left) >>> 1;
            if (nums[mid] >= x) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return result;
    }
}