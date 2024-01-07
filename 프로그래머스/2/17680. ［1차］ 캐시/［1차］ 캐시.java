import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        if (cacheSize == 0) {
            return cities.length * 5;
        }
        Queue<String> q = new LinkedList<>();
        int answer = 0;
        
        for(String city : cities) {
            city = city.toLowerCase();
            
            if (q.contains(city)) {
                q.remove(city);
                q.add(city);
                answer++;
            } else {
                answer += 5;
                if (q.size() == cacheSize) {
                    q.poll();       
                }
                q.add(city);
            }
        }
        
        return answer;
        
    }
}