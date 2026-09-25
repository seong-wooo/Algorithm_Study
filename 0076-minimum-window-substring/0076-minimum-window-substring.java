class Solution {
    public String minWindow(String s, String t) {
        if (t.length() > s.length()) {
            return "";
        }

        Map<Character, Integer> counter = new HashMap<>();

        for (char c : t.toCharArray()) {
            counter.merge(c, 1, Integer::sum);
        }

        int missing = counter.size();
        int left = 0;
        String answer = "";
        int minSize = s.length() + 1;

        char[] ch = s.toCharArray();
        for (int right = 0; right < ch.length; right++) {
            if (counter.containsKey(ch[right])) {
                counter.put(ch[right], counter.get(ch[right]) - 1);
                if (counter.get(ch[right]) == 0) {
                    missing--;
                }
                while (missing == 0) {
                    if (minSize > right - left + 1) {
                        minSize = right - left + 1;
                        answer = s.substring(left, right+1);
                    }
                    if (counter.containsKey(ch[left])) {
                        counter.put(ch[left], counter.get(ch[left]) + 1);
                        if (counter.get(ch[left]) == 1) {
                            missing++;
                        }
                    }
                    left++;
                }
            }
        }

        return answer;
    }
}