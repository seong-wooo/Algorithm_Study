class Solution {
    public int maximumDetonation(int[][] bombs) {
        int answer = 0;

        Map<Integer, List<Integer>> m = new HashMap<>();
        for (int i = 0; i < bombs.length; i++) {
            m.put(i, new ArrayList<>());
        }

        for (int j = 0; j < bombs.length-1; j++) {
            for (int i = j + 1; i < bombs.length; i++) {
                int[] b1 = bombs[j];
                int[] b2 = bombs[i];

                double distance = Math.sqrt(((long) (b1[0] - b2[0]))*(b1[0] - b2[0]) + ((long)(b1[1] - b2[1]))*(b1[1] - b2[1]));

                if (distance <= b1[2]) {
                    m.get(j).add(i);
                }

                if (distance <= b2[2]) {
                    m.get(i).add(j);
                }
            }
        }

        for (int b : m.keySet()) {
            Set<Integer> visited = new HashSet<>();
            Queue<Integer> q = new ArrayDeque<>();
            q.add(b);

            while (!q.isEmpty()) {
                int next = q.poll();
                if (!visited.contains(next)) {
                    visited.add(next);
                    q.addAll(m.get(next));
                }
            }
            answer = Math.max(answer, visited.size());
        }

        return answer;
    }
}