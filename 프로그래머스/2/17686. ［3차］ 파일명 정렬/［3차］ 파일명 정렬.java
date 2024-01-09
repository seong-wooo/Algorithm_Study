import java.util.*;
import java.util.regex.*;

class Solution {
    public String[] solution(String[] files) {
        Pattern pattern = Pattern.compile("(\\D+)(\\d+)(.*)");
        
        Arrays.sort(files, (a, b) -> {
            Matcher ma = pattern.matcher(a.toLowerCase());    
            Matcher mb = pattern.matcher(b.toLowerCase());    
            ma.find();
            mb.find();
            
            if (!ma.group(1).equals(mb.group(1)) ) {
                return ma.group(1).compareTo(mb.group(1));
            }

            return Integer.parseInt(ma.group(2)) - Integer.parseInt(mb.group(2));
        });
        
        return files;
    }
}