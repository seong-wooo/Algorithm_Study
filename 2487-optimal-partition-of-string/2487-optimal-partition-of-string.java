class Solution {
    public int partitionString(String s) {
        int result = 0;
        Set<Character> set = new HashSet<>();

        for (int i = 0; i < s.length(); i++) {
            if (!set.contains(s.charAt(i))) {
                set.add(s.charAt(i));
            } else {
                set.clear();
                set.add(s.charAt(i));
                result++;
            }
        }

        return result + 1;
    }
}