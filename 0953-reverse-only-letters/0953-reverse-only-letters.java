class Solution {
    public String reverseOnlyLetters(String s) {
        int left = 0;
        int right = s.length() - 1;
        char[] c = s.toCharArray();
        
        while (left < right) {
            while (left < right && !Character.isLetter(c[left])) {
                left++;
            }
            while (left < right && !Character.isLetter(c[right])) {
                right--;
            }

            char temp = c[left];
            c[left] = c[right];
            c[right] = temp;
            left++;
            right--;
        }

        StringBuilder sb = new StringBuilder();

        for (char a : c) {
            sb.append(a);
        }
        return sb.toString();
    }
}