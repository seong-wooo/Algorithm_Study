class Solution {
    public int solution(String s) {
        int answer = s.length();
        
        for (int length = 1; length < s.length() / 2 + 1; length++) {
            int i = 0;
            int result = s.length();
            
            while (i <= s.length() - length * 2) {
                int press = 0;
                while (i <= s.length() - length * 2 && s.substring(i, i+length).equals(s.substring(i+length, i+2*length))) {
                    i += length;
                    press++;
                }
                
                if (press > 0) {
                    result -= press * length - String.valueOf(press+1).length();
                } else {
                    i += length;
                }
            }
            answer = (int) Math.min(answer, result);
            
        }
        
        
        
        return answer;
    }
}