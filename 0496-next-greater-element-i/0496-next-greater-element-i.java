class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Deque<Integer> stack = new ArrayDeque<>();
        Map<Integer, Integer> next = new HashMap<>();

        for (int n : nums2) {
            next.put(n, -1);
            while (!stack.isEmpty() && stack.peek() < n) {
                int prev = stack.pop();
                next.put(prev, n);
            }
            stack.push(n);
        }

        int[] answer = new int[nums1.length];

        for (int i = 0; i < nums1.length; i++) {
            answer[i] = next.get(nums1[i]);
        }

        return answer;
    }
}