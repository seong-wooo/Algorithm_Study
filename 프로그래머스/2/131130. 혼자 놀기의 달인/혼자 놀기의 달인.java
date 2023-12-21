import java.util.*;

class Solution {
    public int solution(int[] cards) {
        boolean[] visited = new boolean[cards.length];
        List<Integer> groups = new ArrayList<>();
        
        for (int i = 0; i < visited.length; i++) {
            if (!visited[i]) {
                int group = 0;
                int j = i;
                while(!visited[j]) {
                    group++;
                    visited[j] = true;
                    j = cards[j] - 1;
                }
                groups.add(group);
            }
        }
        
        if (groups.size() == 1) {
            return 0;
        }
        
        groups.sort(Comparator.reverseOrder());
        return groups.get(0) * groups.get(1);
        
    }
}