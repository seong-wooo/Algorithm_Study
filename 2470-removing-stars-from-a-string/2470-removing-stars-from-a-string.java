class Solution {
    public String removeStars(String s) {
        char[] answer = new char[s.length()];
        int index = 0;

        for (char c : s.toCharArray()) {
            if (c == '*') {
                index = Math.max(0, index - 1);
            } else {
                answer[index++] = c;
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < index; i++) {
            sb.append(answer[i]);
        }

        return sb.toString();
    }
}