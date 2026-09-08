class Solution {
    private final List<String> answer = new ArrayList<>();
    private final Map<Character, char[]> d = Map.of(
            '2', new char[]{'a', 'b', 'c'},
            '3', new char[]{'d', 'e', 'f'},
            '4', new char[]{'g', 'h', 'i'},
            '5', new char[]{'j', 'k', 'l'},
            '6', new char[]{'m', 'n', 'o'},
            '7', new char[]{'p', 'q', 'r', 's'},
            '8', new char[]{'t', 'u', 'v'},
            '9', new char[]{'w', 'x', 'y', 'z'}
        );

    public List<String> letterCombinations(String digits) {
       dfs(digits, new StringBuilder());

       return answer;
    }

    public void dfs(String digits, StringBuilder sb) {
        if (digits.length() == sb.length()) {
            answer.add(sb.toString());
            return;
        }
        
        char[] letters = d.get(digits.charAt(sb.length()));

        for (char l : letters) {
            sb.append(l);
            dfs(digits, sb);
            sb.setLength(sb.length() - 1);
        }
    }
}