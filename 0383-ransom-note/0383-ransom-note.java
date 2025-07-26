class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> r = new HashMap<>();
        Map<Character, Integer> m = new HashMap<>();


        for (char c : ransomNote.toCharArray()) {
            r.merge(c, 1, (o,v) -> o + 1);
        }
        for (char c : magazine.toCharArray()) {
            m.merge(c, 1, (o,v) -> o + 1);
        }

        for(char c : r.keySet()) {
            if (r.get(c) > m.getOrDefault(c, 0)) {
                return false;
            }
        }
        return true;
    }
}