class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] counter = new int[numCourses];
        Map<Integer, List<Integer>> courses = new HashMap<>();
        Queue<Integer> q = new ArrayDeque<>();

        for (int[] p : prerequisites) {
            counter[p[0]]++;
            courses.computeIfAbsent(p[1], k -> new ArrayList<>()).add(p[0]);
        }

        for (int i = 0; i < numCourses; i++) {
            if (counter[i] == 0) {
                q.offer(i);
            }
        }

        while (!q.isEmpty()) {
            int course = q.poll();
            List<Integer> next = courses.getOrDefault(course, List.of());
            for (int n : next) {
                if (--counter[n] == 0) {
                    q.offer(n);
                }
            }
        }

        for (int c : counter) {
            if (c > 0) {
                return false;
            }
        }
        return true;
    }
}