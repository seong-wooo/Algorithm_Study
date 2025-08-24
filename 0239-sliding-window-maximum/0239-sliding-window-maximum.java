class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Queue<Integer> pq = new PriorityQueue<>(
            (a, b) -> nums[b] - nums[a]
        );

        for (int i = 0; i < k; i++) {
            pq.add(i);
        }

        List<Integer> answer = new ArrayList<>();
        for (int i = k - 1; i < nums.length; i++) {
            while (!pq.isEmpty() && pq.peek() <= i - k) {
                pq.poll();
            }

            pq.add(i);
            answer.add(nums[pq.peek()]);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}