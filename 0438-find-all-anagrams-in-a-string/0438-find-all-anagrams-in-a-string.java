class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] count = new int[26];

        for(char c : p.toCharArray()) {
            count[c - 'a']++;
        }

        int left = 0;
        List<Integer> answer = new ArrayList<>();
        for (int right = 0; right < s.length(); right++) {
            int index = s.charAt(right) - 'a';
            count[index]--;
            while(count[index] < 0) {
                count[s.charAt(left++) - 'a']++;
            }

            if (right - left +1 ==p.length()) {
                answer.add(left);
            }
        }
        return answer;
    }
}