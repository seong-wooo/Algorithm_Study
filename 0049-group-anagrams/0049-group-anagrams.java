class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> m = new HashMap<>();

        for (String s : strs) {
            char[] ch = new char[26];

            for(char c : s.toCharArray()) {
                ch[c - 'a']++;
            }

            m.computeIfAbsent(new String(ch), x -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(m.values());
    }
}