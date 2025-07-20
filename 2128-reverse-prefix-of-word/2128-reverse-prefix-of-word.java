class Solution {
    public String reversePrefix(String word, char ch) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == ch) {
                sb.append(ch);
                return sb.reverse().toString() + word.substring(i+1);
            }
            sb.append(word.charAt(i));
        }

        return word;
    }
}