import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s) {
        int[] nums = Arrays.stream(s.split(" "))
            .mapToInt(Integer::valueOf)
            .toArray();
        int max = nums[0];
        int min = nums[0];
        
        for (int i = 0; i < nums.length; i++) {
            if (max < nums[i]) {
                max = nums[i];
            }
            if (min > nums[i]) {
                min = nums[i];
            }
        }
        
        return String.format("%d %d", min, max);
    }
}