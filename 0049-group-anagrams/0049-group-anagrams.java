class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> ana = new HashMap<>();

        for (String str : strs) {
            
            char[] count = new char[26];
            for (char c : str.toCharArray()) {
                count[c-'a']++;
            }
            ana.computeIfAbsent(new String(count), k -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(ana.values());
    }
}