import java.util.*;

class Solution {
    public int[] solution(String msg) {
        Map<String, Integer> dict = new HashMap<>();
        for (int index = 1; index < 27; index++) {
            dict.put(String.valueOf((char) (index + 64)), index);
        }
    
        int left = 0;
        int next_index = 27;
        List<Integer> answer = new ArrayList<>();
        
        while (left < msg.length()) {
            int right = left + 1;
            while (right <= msg.length() && dict.containsKey(msg.substring(left, right))) {
                right++;
            }
            
            if (right == msg.length() + 1) {
                answer.add(dict.get(msg.substring(left)));
                break;
            }
            dict.put(msg.substring(left, right), next_index);
            next_index++;
            answer.add(dict.get(msg.substring(left,right-1)));
            left = right - 1;
            
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}