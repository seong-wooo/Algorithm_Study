import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        Map<String, Integer> times = new HashMap<>();
        Map<String, Integer> park = new HashMap<>();
        
        for (String record : records) {
            String[] s = record.split(" ");
            int minute = changeTime(s[0]);
            String num = s[1];
            
            if(s[2].equals("IN")) {
                park.put(num, minute);
            } else {
                int inTime = park.remove(num);
                times.merge(num, minute - inTime, (o, v) -> o + v);
            }
        }
        int maxTime = changeTime("23:59");
        
        for (Map.Entry<String,Integer> kv : park.entrySet()) {
            times.merge(kv.getKey(), maxTime - kv.getValue(), (o, v) -> o + v);
        }

        return times.entrySet().stream()
            .sorted(Map.Entry.comparingByKey())
            .mapToInt(entry -> fees[1] + (int) Math.ceil(Math.max(0, times.get(entry.getKey()) - fees[0]) / (double)fees[2]) * fees[3])
            .toArray();
    }
    
    public int changeTime(String time) {
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }
}