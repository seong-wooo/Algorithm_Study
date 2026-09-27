class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] counter = new int[26];
        List<Integer> answer = new ArrayList<>();
        // missing == 0 이라면 anagram 있는거임
        // counter 가 0보다 커지면 missing++ 
        // counter 가 0이 되면 missing--
        
        int missing = 0;
        for(char c : p.toCharArray()) {
            if (++counter[c - 'a'] == 1) {
                missing++;
            }
        }
        int left = 0;
        char[] ch = s.toCharArray();

        for(int right = 0; right < ch.length; right++) {
            int index = ch[right] - 'a';
            if (--counter[index] == 0) {      // 이 글자가 필요한 만큼 다 채워졌다
                missing--;
            }
            while(counter[index] < 0) {
                if (++counter[ch[left++] - 'a'] == 1) {
                    missing++;
                }
            }

            if (missing == 0) {
                answer.add(left); 
            }
        }

        return answer;
    }
}