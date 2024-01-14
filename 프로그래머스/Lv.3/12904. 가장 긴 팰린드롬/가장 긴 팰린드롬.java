class Solution
{
    public int solution(String s) {
        int answer = 1;
        for(int i = 0; i < s.length() - 1; i++) {
            for (int j = i+1; j < s.length(); j++) {
               if(isPalindrome(s, i, j) && answer < j - i + 1) {
                   answer = j - i + 1;
               }
            }
        }
        return answer;
    }
    
    public boolean isPalindrome(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
}