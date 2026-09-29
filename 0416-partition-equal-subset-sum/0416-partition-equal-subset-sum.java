class Solution {
    public boolean canPartition(int[] nums) {
        // boolean[] 
        // i 마다 boolean다 돌면서 true 인 인덱스 + n
        int total = 0;
        for(int i = 0; i < nums.length; i++) {
            total += nums[i];
        }

        if ((total&1) == 1) {
            return false;
        }
        int target = total / 2;

        boolean[] result = new boolean[target + 1];
        result[0] = true;

        for (int n : nums) {
            for(int i = target - n; i >= 0; i--) {
                if (result[i]) {
                    int next = i + n;
                    if (next == target) {
                        return true;
                    } else if (next < target) {
                        result[next] = true;
                    }
                }
            }
        }
        return false;
    }
}