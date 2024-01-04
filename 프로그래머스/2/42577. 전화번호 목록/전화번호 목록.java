import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book, (a, b) -> a.length() - b.length());
        
        Set<String> s = new HashSet<>();
        
        for (String p : phone_book) {
            for (int i = 1; i < p.length() + 1; i++) {
                if (s.contains(p.substring(0, i))) {
                    return false;
                }
            }
            s.add(p);
        }
        
        return true;
    }
}