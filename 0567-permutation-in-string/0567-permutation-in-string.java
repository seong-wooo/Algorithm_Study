class Solution {
    public boolean checkInclusion(String s1, String s2) {
        Map<Character, Integer> counter = new HashMap<>();
        for (char c1 : s1.toCharArray()) {
            counter.merge(c1, 1, Integer::sum);
        }
        
        int left = 0;
        char[] c2 = s2.toCharArray();

        for (int right = 0; right < c2.length; right++) {
            // 키 없다 -> left = right 까지
            // 키 있다 -> 음수라면 양수가 될 때 까지 left ++
        //                길이 확인에서 맞으면 true

            if (!counter.containsKey(c2[right])) {
                for (int i = left; i < right; i++) {
                    if (counter.containsKey(c2[i])) {
                        counter.put(c2[i], counter.get(c2[i]) + 1);
                    }
                }
                left = right + 1;
            } else {
                counter.put(c2[right], counter.get(c2[right]) - 1);

                while(counter.get(c2[right]) < 0) {
                    if (counter.containsKey(c2[left])) {
                        counter.put(c2[left], counter.get(c2[left]) + 1);
                    }
                    left++;
                }
                
                if (right - left + 1 == s1.length()) {
                    return true;
                }
            }

        }
        return false;
    }
}