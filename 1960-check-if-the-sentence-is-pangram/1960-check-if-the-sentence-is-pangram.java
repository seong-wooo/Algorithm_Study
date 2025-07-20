class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] pang = new boolean[26];

        for (char c : sentence.toCharArray()) {
            pang[c - 'a'] = true;
        }

        for (boolean p : pang) {
            if (!p) {
                return p;
            }
        }
        return true;

    }
}