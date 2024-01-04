import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = Arrays.stream(numbers)
            .mapToObj(String::valueOf)
            .sorted(new Comparator<String>() {
                @Override
                public int compare(String a, String b) {
                    a = a.repeat(4);
                    b = b.repeat(4);
                    
                    for (int i = 0; i < 4; i++) {
                        if (a.charAt(i) < b.charAt(i)) {
                            return 1;
                        } else if (a.charAt(i) > b.charAt(i)) {
                            return -1;
                        }
                    }
                    return 0;
                }
            })
            .collect(Collectors.joining());
        
        return answer.charAt(0) != '0' ? answer : "0";
    }
}