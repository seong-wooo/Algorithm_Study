class Solution {
    boolean solution(String s) {
        int x = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                x++;
                continue;
            } else if (x == 0) {
                return false;
            }
            x--;
        }
        
        return x == 0;
    }
}