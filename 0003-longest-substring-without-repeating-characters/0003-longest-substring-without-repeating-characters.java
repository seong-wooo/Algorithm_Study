class Solution {
    public int lengthOfLongestSubstring(String s) {
        Queue<Character> q = new LinkedList<>();
        Set<Character> st = new HashSet<>();

        int answer = 0;

        for (char c : s.toCharArray()) {
            while(st.contains(c)) {
                st.remove(q.poll());
            }

            q.offer(c);
            st.add(c);
            answer = Math.max(answer, q.size());
        }
        return answer;
    }
}