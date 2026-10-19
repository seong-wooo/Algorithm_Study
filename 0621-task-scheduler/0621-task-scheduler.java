class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> counter = new HashMap<>();

        for(char task : tasks) {
            counter.merge(task, 1, Integer::sum);
        }

        int maxCount = 0;
        int maxTasks = 0;

        for (char task : counter.keySet()) {
            if (maxCount < counter.get(task)) {
                maxCount = counter.get(task);
                maxTasks = 1;
            } else if (maxCount == counter.get(task)) {
                maxTasks++;
            }
        }

        return Math.max(tasks.length, (maxCount - 1) * (n + 1) + maxTasks);
    }
}