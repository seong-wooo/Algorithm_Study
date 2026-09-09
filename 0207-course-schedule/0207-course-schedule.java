class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> maps = new HashMap<>();
        int[] counts = new int[numCourses];
        Set<Integer> total = new HashSet<>();

        for (int[] p : prerequisites) {
            maps.computeIfAbsent(p[0], k -> new ArrayList<>()).add(p[1]);
            counts[p[1]]++;
            total.add(p[0]);
            total.add(p[1]);
        }

        Queue<Integer> q = new LinkedList<>();

        for (int i : total) {
            if (counts[i] == 0) {
                q.offer(i);
            }
        }

        while(!q.isEmpty()) {
            int c = q.poll();
            if (!maps.containsKey(c)) {
                continue;
            }

            List<Integer> next= maps.get(c);
            for (int n : next) {
                counts[n]--;
                if (counts[n] == 0) {
                    q.offer(n);
                }
            }
        }
        for (int t : total) {
                if (counts[t] != 0) {
                    return false;
                }
            }
        return true;
    }
}