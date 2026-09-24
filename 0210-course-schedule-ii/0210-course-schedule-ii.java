class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] counter = new int[numCourses];
        List<List<Integer>> graph = new ArrayList<>(numCourses);

        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] p : prerequisites) {
            counter[p[0]]++;
            graph.get(p[1]).add(p[0]);
        }

        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (counter[i] == 0) {
                q.add(i);
            }
        }

        int[] order = new int[numCourses];
        int taken = 0;
        while (!q.isEmpty()) {
            int course = q.poll();
            order[taken++] = course;

            for(int next : graph.get(course)) {
                if (--counter[next] == 0) {
                    q.add(next);
                }
            }
        }

        return taken == numCourses ? order : new int[0];
    }
}