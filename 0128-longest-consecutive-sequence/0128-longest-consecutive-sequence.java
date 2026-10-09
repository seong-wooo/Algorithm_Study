class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numset = new HashSet<>();

        for(int num : nums) {
            numset.add(num);
        }

        int answer = 0;

        for (int num : numset) {
            if (!numset.contains(num - 1)) {
                int current = num;
                int count = 1;

                while (numset.contains(current + 1)) {
                    current++;
                    count++;
                }

                answer = Math.max(count, answer);
            }
        }

        return answer; 
    }
}