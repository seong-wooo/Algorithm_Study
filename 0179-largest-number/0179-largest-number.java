class Solution {
    public String largestNumber(int[] nums) {
        String result = Arrays.stream(nums).mapToObj(num -> num).sorted(
            (a, b) -> {
            StringBuilder sb1 = new StringBuilder();
            StringBuilder sb2 = new StringBuilder();

            while (sb1.length() < 11) {
                sb1.append(String.valueOf(a));
            }
            sb1.setLength(11);

            while (sb2.length() < 11) {
                sb2.append(String.valueOf(b));
            }
            sb2.setLength(9);

            return sb2.toString().compareTo(sb1.toString());
        })
        .map(String::valueOf)
        .collect(Collectors.joining());

        return result.startsWith("0") ? "0" : result;
    }
}