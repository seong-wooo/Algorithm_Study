import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int result = n;
        
        for (int i = 0; i < wires.length; i++) {
            Set<Integer> nodes = new HashSet<>();
            if (i != 0) {
                nodes.add(wires[0][0]);
                nodes.add(wires[0][1]);
            } else {
                nodes.add(wires[1][0]);
                nodes.add(wires[1][1]);
            }

            for (int j = 0; j < wires.length; j++) {
                for (int k = 0; k < wires.length; k++) {
                    if (i != k) {
                        if (nodes.contains(wires[k][0]) || nodes.contains(wires[k][1])) {
                            nodes.add(wires[k][0]);
                            nodes.add(wires[k][1]);
                        }
                    }
                }
            }
            result = (int) Math.min(result, Math.abs(n - 2 * nodes.size()));
        }
        return result;
    }
}