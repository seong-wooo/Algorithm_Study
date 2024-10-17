import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(int[] numbers) {
        String result = Arrays.stream(numbers)
            .mapToObj(String::valueOf)
            .sorted((a, b) -> (b+a).compareTo(a+b))
            .collect(Collectors.joining());
        
        return result.charAt(0) == '0' ? "0" : result;
    }
}