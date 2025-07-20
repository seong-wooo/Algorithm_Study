class Solution {
    public int maxVowels(String s, int k) {
        int answer = 0;
        int current = 0;
        Set<Character> hs = Set.of('a', 'e', 'i', 'o', 'u');

        for (int i = 0; i < s.length(); i++) {
            if (hs.contains(s.charAt(i))) {
                current++;
            }
            if (i >= k && hs.contains(s.charAt(i - k))) {
                current--;
            }
            answer = (int) Math.max(current, answer);
        }

        return answer;
    }
}