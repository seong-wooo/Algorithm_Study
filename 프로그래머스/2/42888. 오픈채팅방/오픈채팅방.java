import java.util.*;
import java.util.stream.*;

class Solution {
    public String[] solution(String[] record) {
        Map<String, String> idName = new HashMap<>();
        List<String[]> answer = new ArrayList<>();
        String[] mention = new String[]{"님이 들어왔습니다.", "님이 나갔습니다."};
        
        for (String r : record) {
            String[] s = r.split(" ");
            if (s[0].equals("Leave")) {
                answer.add(new String[]{s[1], mention[1]});
            }
            else {
                idName.put(s[1], s[2]);
                if (s[0].equals("Enter")) {
                    answer.add(new String[]{s[1], mention[0]});
                }
            }
        }
        
        
        return answer.stream()
            .map(s -> idName.get(s[0]) + s[1])
            .toArray(String[]::new);
    }
}