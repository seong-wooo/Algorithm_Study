class Solution {
    public int maxVowels(String s, int k) {
        Set<Character> m = Set.of('a', 'e', 'i', 'o', 'u');

        int answer = 0;
        char[] ch = s.toCharArray();
        for (int i = 0; i < k; i++) {
            if (m.contains(ch[i])) {
                answer++;
            }
        }
        
        int current = answer;
        for (int i = k; i < ch.length; i++) {
            if (m.contains(ch[i - k])) {
                current--;
            }

            if (m.contains(ch[i])) {
                current++;
            }
            answer = (int) Math.max(answer, current);
        }

        return answer;
    }
}