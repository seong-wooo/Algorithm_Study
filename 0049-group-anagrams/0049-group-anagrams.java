class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagram = new HashMap<>();

        for(String str: strs) {
            char[] ch = str.toCharArray();
            Arrays.sort(ch);
            String ana = new String(ch);

            anagram.computeIfAbsent(ana, k -> new ArrayList<>()).add(str);
        }


        return new ArrayList<>(anagram.values());

    }
}