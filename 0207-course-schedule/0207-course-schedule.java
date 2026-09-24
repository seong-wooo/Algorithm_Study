class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] counter = new int[numCourses];
        List<List<Integer>> graph = new ArrayList<>(numCourses);

        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }


        for (int[] p : prerequisites) {
            graph.get(p[1]).add(p[0]);
            counter[p[0]]++;
        }

        Queue<Integer> q = new ArrayDeque<>();

        for (int i = 0; i < numCourses; i++) {
            if (counter[i] == 0) {
                q.offer(i);
            }
        }

        int taken = 0;
        while (!q.isEmpty()) {
            int course = q.poll();
            taken++;

            for (int n : graph.get(course)) {
                if (--counter[n] == 0) {
                    q.offer(n);
                }
            }
        }

        return taken == numCourses;
    }
}