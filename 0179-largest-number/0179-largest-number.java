class Solution {
    public String largestNumber(int[] nums) {
        String answer = Arrays.stream(nums)
        .mapToObj(String::valueOf)
        .sorted((a, b) -> (b + a).compareTo((a + b)))
        .collect(Collectors.joining());

        return answer.charAt(0) == '0' ? "0" : answer;
    }
}