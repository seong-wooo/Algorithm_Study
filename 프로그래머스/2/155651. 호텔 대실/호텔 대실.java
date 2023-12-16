import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(String[][] book_time) {
        List<int[]> bookTimes = Arrays.stream(book_time)
            .map(times -> {
                String[] start = times[0].split(":");
                int startTime = Integer.parseInt(start[0]) * 60 + Integer.parseInt(start[1]);
                
                String[] end = times[1].split(":");
                int endTime = Integer.parseInt(end[0]) * 60 + Integer.parseInt(end[1]) + 10;
                
                return new int[]{startTime, endTime};  
            })
            .sorted(Comparator.comparingInt((int[] x) -> x[0]))
            .collect(Collectors.toList());
        
        
        List<Integer> room = new ArrayList<>();
        
        for(int[] bookTime : bookTimes) {
            int start = bookTime[0];
            int end = bookTime[1];
            boolean isAvailable = false;
            for (int i = 0; i < room.size(); i++) {
                if (start >= room.get(i)) {
                    room.set(i, end);
                    isAvailable = true;
                    break;
                }
            }
            
            if (!isAvailable) {
                room.add(end);
            }
        }
        
        
        
        return room.size();
        
    }
}