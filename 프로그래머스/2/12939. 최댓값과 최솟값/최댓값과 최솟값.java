import java.util.*;

class Solution {
    public String solution(String s) {
        String[] ss = s.split(" ");
        Arrays.sort(ss, (a,b) -> Integer.valueOf(a) - Integer.valueOf(b));
        
        return ss[0] + " " + ss[ss.length - 1];
    }
}