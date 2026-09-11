class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> n1 = new HashSet<>();
        List<Integer> answer = new ArrayList<>();

        for (int n : nums1) {
            n1.add(n);
        }

        for (int n : nums2) {
            if (n1.contains(n)) {
                answer.add(n);
                n1.remove(n);
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}