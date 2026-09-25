class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        List<int[]> answer = new ArrayList<>();

        for(int[] itv : intervals) {
            if (answer.isEmpty()) {
                answer.add(itv);
            } else {
                int[] last = answer.get(answer.size() - 1);
                if (last[1] >= itv[0]) {
                    last[1] = Math.max(last[1], itv[1]);
                } else {
                    answer.add(itv);
                }
            }
        }

        return answer.toArray(new int[0][]);
    }
}