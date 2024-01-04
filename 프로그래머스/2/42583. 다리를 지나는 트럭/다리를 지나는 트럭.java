import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<int[]> q = new LinkedList<>();
        int w = 0;
        int time = 1;
        
        for (int truck : truck_weights) {
            while(!q.isEmpty() && time - q.peekFirst()[1] >= bridge_length || w + truck > weight) {
                int[] tt = q.pollFirst();
                w -= tt[0];
                time = tt[1] + bridge_length;
            }
            q.add(new int[]{truck, time});
            w += truck;
            time += 1;
        }
        return q.peekLast()[1] + bridge_length;
    }
}