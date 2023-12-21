import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        return LongStream.rangeClosed(left, right)
                .map(x -> Math.max(x / n, x % n) + 1)
                .mapToInt(x -> (int) x)
                .toArray();
    }
}