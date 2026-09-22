class Solution {
    public int totalFruit(int[] fruits) {
        int left = 0;
        Map<Integer, Integer> count = new HashMap<>();
        int answer = 0;
        for (int right = 0; right < fruits.length; right++) {
            count.merge(fruits[right], 1, Integer::sum);

            while (count.size() > 2) {
                if (count.merge(fruits[left], -1, Integer::sum) == 0) {
                    count.remove(fruits[left]);
                }
                left++;
            }

            answer = Math.max(answer, right - left + 1);
        }
        return answer;
    }
}