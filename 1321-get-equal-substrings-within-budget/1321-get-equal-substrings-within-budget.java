class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int currentCost = 0;
        int answer = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            currentCost += Math.abs(s.charAt(right) - t.charAt(right));

            if (currentCost <= maxCost) {
                answer = Math.max(answer, right - left + 1);
            }

            while(currentCost > maxCost) {
                currentCost -= Math.abs(s.charAt(left) - t.charAt(left));
                left++;
            }
        }

        return answer;
    }
}