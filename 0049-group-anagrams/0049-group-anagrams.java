class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagram = new HashMap<>();

        for(String str: strs) {
            
            char[] ch = new char[26];
            for (char c : str.toCharArray()) {
                ch[c - 'a']++;
            }
            String ana = new String(ch);

            anagram.computeIfAbsent(ana, k -> new ArrayList<>()).add(str);
        }


        return new ArrayList<>(anagram.values());

    }
}