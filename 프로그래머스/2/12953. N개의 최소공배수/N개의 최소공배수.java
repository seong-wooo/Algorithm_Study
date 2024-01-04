import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] arr) {        
        return Arrays.stream(arr)
            .reduce(1, (a, b) -> a * b / gcd(a, b));
    }
    
    public int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}