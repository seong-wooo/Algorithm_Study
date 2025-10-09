class Solution {
    public int videoStitching(int[][] clips, int time) {
        int[] times = new int[101];

        for (int[] clip : clips) {
            times[clip[0]] = (int) Math.max(times[clip[0]], clip[1]);
        }
        
        int count = 0;
        int currentEnd = 0;
        int nextEnd = 0;

        for (int i = 0; i <= time; i++) {
            // i가 현재 덮을 수 있는 범위를 넘어갔는데 nextEnd로도 못 가면 불가능
            if (i > nextEnd) return -1;

            // i가 현재 덮은 범위 끝이면 새로운 구간을 추가해야 함
            if (i > currentEnd) {
                count++;
                currentEnd = nextEnd;
            }

            // i에서 시작할 수 있는 clip 중 가장 멀리 가는 곳으로 nextEnd 갱신
            nextEnd = Math.max(nextEnd, times[i]);
        }

        return count;
    }
}