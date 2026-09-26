class Solution {
    public String reorganizeString(String s) {
        int[] counter = new int[26];
        
        char[] ch = s.toCharArray();
        int half = (s.length() + 1) / 2;
        
        int max = 0;
        for (char c : ch) {
            counter[c - 'a']++;
            if (counter[c - 'a'] > counter[max]) {
                max = c - 'a';
            }
        }

        if (counter[max] > half) {
            return "";
        }


        char[] result = new char[s.length()];
        char c = (char) (max + 'a');

        for (int even = 0; even < s.length(); even+=2) {
            if (counter[c - 'a'] == 0) {
                for (int i = 0; i < 26; i++) {
                    if (counter[i] > 0) {
                        c = (char) (i + 'a');
                    }
                }
            }

            result[even] = c;
            counter[c - 'a']--;
        }

        for (int odd = 1; odd < s.length(); odd+=2) {
            if (counter[c - 'a'] == 0) {
                for (int i = 0; i < 26; i++) {
                    if (counter[i] > 0) {
                        c = (char) (i + 'a');
                    }
                }
            }

            result[odd] = c;
            counter[c - 'a']--;
        }

        return new String(result);
    }
}