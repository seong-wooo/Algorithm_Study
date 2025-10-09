class Solution {
    public long makeIntegerBeautiful(long n, int target) {
        String s = String.valueOf(n);

        int[] nums = new int[s.length()]; 

        for (int i = 0; i < s.length(); i++) {
            nums[i] = s.charAt(s.length() - 1 - i) - 48;
        }


        int index = 0;
        long answer = 0;
        while(!isValid(nums, target) && index < s.length()) {
            answer += (10 - nums[index]) * Math.pow(10, index);
            nums[index] = 0;
            if (index < s.length() - 1) {
                nums[index + 1]++;
            }
            index++;
            System.out.println(answer);
        }
        return answer;
    }

    public boolean isValid(int[] nums, int target) {
        for (int num : nums) {
            target -= num;

            if (target < 0) {
                return false;
            }
        }

        return true;
    }
}