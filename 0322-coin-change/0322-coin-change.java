class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) {
            return 0;
        }
        int[] counter = new int[amount + 1];
        Arrays.fill(counter, Integer.MAX_VALUE);

        Arrays.sort(coins);
        for (int c : coins) {
            if (c <= amount) {
                counter[c] = 1;
            }
        }

        for (int i = 1; i <= amount; i++) {
            if(counter[i] == Integer.MAX_VALUE) {
                for (int j = 0; j < coins.length && coins[j] <= i; j++) {
                    if (counter[i - coins[j]] != Integer.MAX_VALUE) {
                        counter[i] = Math.min(counter[i], counter[i - coins[j]] + 1);
                    }
                }
            }
        }
        return counter[amount] == Integer.MAX_VALUE ? -1 : counter[amount];
    }
}