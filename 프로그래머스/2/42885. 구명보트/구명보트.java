import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        int f = 0;
        int b = people.length - 1;
        
        Arrays.sort(people);
        
        while (f <= b) {
            answer++;
            if (people[f] + people[b] <= limit) {
                f++;
            }
            b--;
        }
        
        return answer;
    }
}