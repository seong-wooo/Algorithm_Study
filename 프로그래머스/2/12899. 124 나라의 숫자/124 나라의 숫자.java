class Solution {
    public String solution(int n) {
        StringBuilder sb = new StringBuilder();
        String[] nums = new String[]{"4", "1", "2"};
        
        while (n > 0) {
            int c = n % 3;
            sb.append(nums[c]);
            n -= c != 0 ? c : 3;
            n /= 3;
        }
        
        return sb.reverse().toString();
    }
}