class Solution {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, Comparator.comparingInt(x -> x[0]));
        
        // [방번호, 끝나는 시각]
        Queue<int[]> pq1 = new PriorityQueue<>((a, b) -> a[1] - b[1] == 0 ? a[0] - b[0] : a[1] - b[1]);

        // 빈 방 담는 pq [방번호, 끝나는 시각]
        Queue<int[]> pq2 = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            pq1.add(new int[]{i, 0});
        }

        for (int[] meeting : meetings) {
            while (!pq1.isEmpty() && pq1.peek()[1] <= meeting[0]) {
                pq2.add(pq1.poll());
            }
            int[] roomInfo;
            if (!pq2.isEmpty()) {
                roomInfo = pq2.poll();
                roomInfo[1] = meeting[1];
            } else { 
                roomInfo = pq1.poll();
                roomInfo[1] += meeting[1] - meeting[0];
            }
            result[roomInfo[0]]++;

            pq1.add(roomInfo);
        }
        
        int answer = 0;

        for (int i = 1; i < n; i++) {
            if (result[answer] < result[i]) {
                answer = i;
            }
        }
        return answer;
    }
}