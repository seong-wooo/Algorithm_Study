class Solution {
    public int[] solution(String s) {
        int[] answer = {0, 0};
        
        while (!s.equals("1")) {
            int one = 0;
            for (char c : s.toCharArray()) {
                if (c == '1') {
                    one++;
                }
            }
            
            answer[0]++;
            answer[1] += s.length() - one;
            
            StringBuilder sb = new StringBuilder();
            
            while (one > 1) {
                sb.append(Integer.toString(one % 2));
                one = one / 2;
            }
            sb.append(one);
            s = sb.reverse().toString();
            
            
        }
        return answer;
    }
}