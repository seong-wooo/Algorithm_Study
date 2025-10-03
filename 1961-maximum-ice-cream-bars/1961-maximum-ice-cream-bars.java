class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int[] counter = new int[100001];

        for (int cost : costs) {
            counter[cost]++;
        }

        int result = 0;

        for (int i = 1; i < counter.length; i++) {
            if (i > coins) {
                break;
            }
            
            if (counter[i] > 0) {
                int d = (int) Math.min(counter[i], coins / i);
                coins -= d * i;
                counter[i] -= d;
                result += d;

                if (counter[i] != 0) {
                    break;
                }
            }
        }
        return result;
    }
}