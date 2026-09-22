class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> count = new HashMap<>();

        int left = 0;
        int answer = 0;
        for (int right = 0; right < fruits.length; right++) {
            count.merge(fruits[right], 1 ,Integer::sum);

            while (count.size() > 2) {
                int f = fruits[left++];
                if (count.merge(f, -1, Integer::sum) == 0) {
                    count.remove(f);
                }
            }
            answer = Math.max(answer, right - left + 1);
        }       
        return answer;
    }
}

