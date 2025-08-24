class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Queue<int[]> pq = new PriorityQueue<>(
            (a, b) -> b[0] - a[0]
        );

        for (int i = 0; i < k; i++) {
            pq.add(new int[]{nums[i], i});
        }

        List<Integer> answer = new ArrayList<>();
        answer.add(pq.peek()[0]);
        for (int i = k; i < nums.length; i++) {
            while (!pq.isEmpty() && pq.peek()[1] <= i - k) {
                pq.poll();
            }

            pq.add(new int[]{nums[i], i});
            answer.add(pq.peek()[0]);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}