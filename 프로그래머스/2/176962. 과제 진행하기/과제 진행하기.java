import java.util.*;
import java.util.stream.*;

class Solution {
    public String[] solution(String[][] plans) {
        Deque<Subject> ps = Arrays.stream(plans)
            .map(plan -> {
                String[] hm = plan[1].split(":");
                return new Subject(plan[0], Integer.parseInt(hm[0]), Integer.parseInt(hm[1]), Integer.parseInt(plan[2]));
            })
            .sorted(Comparator.comparingInt((Subject s) -> s.hour).thenComparingInt((s) -> s.minute))
            .collect(Collectors.toCollection(LinkedList::new));

        
        Deque<Subject> rest = new LinkedList<>();
        List<String> result = new LinkedList<>();
    
        int[] c = new int[]{ps.peekFirst().hour, ps.peekFirst().minute};
        
        
        while (!ps.isEmpty()) {
            Subject s = ps.pollFirst();
            int d = difference(c[0], c[1], s.hour, s.minute);
            
            // 과제 시작 시간이 안되었다면
            while (d > 0 && !rest.isEmpty()) {

                if (rest.peekFirst().duration > d) {
                    rest.peekFirst().duration -= d;
                    break;
                } else {
                    Subject r = rest.pollFirst();
                    result.add(r.name);
                    d -= r.duration;
                }
            }
            
            c = new int[]{s.hour, s.minute};
            
            if (!ps.isEmpty()) {
                Subject next = ps.peekFirst();
                d = difference(s.hour, s.minute, next.hour, next.minute);
                
                if (d >= s.duration) {
                    int new_minute = s.minute + s.duration;
                    c = new int[]{s.hour + new_minute / 60, new_minute % 60};
                    result.add(s.name);
                } else {
                     int new_minute = s.minute + d;
                    c = new int[]{s.hour + new_minute / 60, new_minute % 60};
                    s.duration -= d;
                    rest.addFirst(s);
                }
            } else {
                result.add(s.name);
            }
                
        }
        result.addAll(rest.stream().map(s -> s.name).collect(Collectors.toList()));
            
            
        return result.toArray(new String[0]);
    }
        
    
    public int difference(int h1, int m1, int h2, int m2) {
        return (h2 - h1) * 60 + m2 - m1;
    }
    
    static class Subject {
        String name;
        int hour;
        int minute;
        int duration;
        
        public Subject(
            String name,
            int hour,
            int minute,
            int duration) {
            this.name = name;
            this.minute = minute;
            this.duration = duration;
            this.hour = hour;
        }
        
        @Override
        public String toString() {
            return String.format("%s %d %d %d", name, hour, minute, duration);
        }
    
    }
}