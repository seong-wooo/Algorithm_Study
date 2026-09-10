class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> answer = new ArrayList<>();
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));


        int[] current = intervals[0];

        for (int[] node : intervals) {
            if (current[1] >= node[0]) {
                current[1] = (int) Math.max(current[1], node[1]);
                continue;
            } else {
                answer.add(current);
                current = node;
            }
        }

        answer.add(current);

        return answer.toArray(int[][]::new);
    }
}