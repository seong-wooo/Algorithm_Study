class Solution {
    public List<Long> maximumEvenSplit(long finalSum) {
        if (finalSum % 2 == 1) {
            return List.of();
        }

        List<Long> result = new LinkedList<>();

        long i = 2;

        while (i <= finalSum) {
            result.add(i);
            finalSum -= i;
            i += 2;
        }

        if (finalSum > 0) {
            result.set(result.size() - 1, result.get(result.size() - 1) + finalSum);
        }
        return result;
    }
}