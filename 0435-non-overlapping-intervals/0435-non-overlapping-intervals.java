class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.<int[]>comparingInt(a -> a[1]));
        int last = Integer.MIN_VALUE;
        int answer = 0;
        for (int[] itv : intervals) {
            if (last > itv[0]) {
                answer++;
            } else {
                last = itv[1];
            }
        }
        return answer;
    }
}