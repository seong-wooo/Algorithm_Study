class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) {
            return 0;
        }

        boolean[] visited = new boolean[amount + 1];

        Queue<int[]> amountCount = new ArrayDeque<>();

        // amount, count
        amountCount.offer(new int[]{0, 0});
        visited[0] = true;
        while (!amountCount.isEmpty()) {
            int[] ac = amountCount.poll();
            int am = ac[0];
            int count = ac[1];

            if (am == amount) {
                return count;
            } 

            for (int coin : coins) {
                if (coin <= amount - am && !visited[coin + am]) {
                    amountCount.add(new int[]{coin + am, count + 1});
                    visited[coin + am] = true;
                }
            }
        }

        return -1;
    }
}