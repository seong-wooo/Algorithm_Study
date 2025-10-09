class Solution {
    public String largestPalindromic(String num) {
        int[] nums = new int[10];

        for (char n : num.toCharArray()) {
            nums[n - 48]++;
        }
        
        StringBuilder sb = new StringBuilder();

        char result = findMaxOddNum(nums);

        if (result != ' ') {
            sb.append(result);
        }

        for (int i = 0; i <= 9; i++) {
            int count = nums[i] / 2;
            String s = String.valueOf((char) (i + '0')).repeat(count);
            sb.insert(0, s);
            sb.append(s);
        }

        String answer = sb.toString();

        if (answer.startsWith("0")) {
            String rz = answer.replace("0", "");
            if (rz.isEmpty()) {
                return "0";
            }
            return rz;
        }
        return answer;
    }
    
    public char findMaxOddNum(int[] nums) {

        for (int i = nums.length -1 ; i >= 0; i--) {
            if (nums[i] % 2 == 1) {
                return (char) (i + '0');
            }
        }

        return ' ';
    }
}