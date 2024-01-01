import java.util.*;
import java.util.stream.*;

class Solution {
    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();
        
        
        for (int i = 0; i < course.length; i++) {
            Map<String, Integer> o = new HashMap<>();
            for(String order : orders) {
                char[] a = order.toCharArray();
                Arrays.sort(a);
                order = new String(a);
                List<String> combs = find(order, course[i]);
                for (String comb : combs) {
                    o.merge(comb, 1, (old, value) -> old + 1);
                }
            }
            if (o.isEmpty()) {
                continue;
            }
            
            int m = o.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .get()
                .getValue();
            
            if (m < 2) {
                continue;
            }
            
            for (Map.Entry<String, Integer> entry : o.entrySet()) {
                if (entry.getValue() == m) {
                    answer.add(entry.getKey());
                }
            }
            
        }
        
        answer.sort(Comparator.naturalOrder());
        
        
        return answer.toArray(new String[0]);
    }
    
    public List<String> find(String origin, int course) {
        if (origin.length() < course) {
            return List.of();
        }
        return findCourse(origin, "", 0, course);
    }
    
    public List<String> findCourse(String origin, String current, int index, int course) {        
        if (course == 0) {
            return List.of(current);
        }
        
        List<String> result = new ArrayList<>();
        
        for (int i = index; i < origin.length() - course + 1; i++) {
            result.addAll(findCourse(origin, current + origin.charAt(i), i + 1, course - 1));
        }
        
        return result;
    }
}