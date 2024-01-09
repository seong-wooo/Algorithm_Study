import java.util.*;
import java.util.stream.*;
import java.util.regex.*;

class Solution {
    public String[] solution(String[] files) {
        return Arrays.stream(files)
            .map(File::new)
            .sorted(Comparator.comparing((File a) -> a.head.toLowerCase()).thenComparingInt((a) -> Integer.parseInt(a.number)))
            .map(File::toString)
            .toArray(String[]::new);
    }
    
    static class File {
        static final Pattern pattern = Pattern.compile("(\\D+)(\\d+)(.*)");
        String head;
        String number;
        String tail;
        
        public File(String file) {
            Matcher matcher = pattern.matcher(file);
            if (matcher.find()) {
                this.head = matcher.group(1);
                this.number = matcher.group(2);
                this.tail = matcher.group(3);   
            }
        }
        
        public String toString() {
            return this.head + this.number + this.tail;
        }
    }
}