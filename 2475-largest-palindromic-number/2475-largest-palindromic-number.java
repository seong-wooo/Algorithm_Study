class Solution {
    public String largestPalindromic(String num) {
        Map<Character, Integer> counter = new HashMap<>();
        Queue<Character> q = new PriorityQueue<>();

        for (char n : num.toCharArray()) {
            if (!counter.containsKey(n)) {
                q.add(n);
                counter.put(n, 0);
            }
            counter.put(n, counter.get(n) + 1);
        }

        // 작은 순으로 꺼낸다.
        // 만약 홀수라면 홀수 개수 제외하고 꺼낸다.
        // 홀수 남은 수는 따로 보관 -> 
        // 0 으로 시작하면 0 제거
        
        StringBuilder sb = new StringBuilder();

        if (hadOddCount(counter)) {
            sb.append(oddCountMaxNum(counter));
        }

        while (!q.isEmpty()) {
            char n = q.poll();
            int p = counter.get(n) / 2;
            String add = String.valueOf(n).repeat(p);

            sb.insert(0, add);
            sb.append(add);
        }

        String answer = sb.toString();

        if (answer.startsWith("0")) {
            String removeZero = answer.replaceAll("0", "");
            if (removeZero.isEmpty()) {
                return "0";
            } else { 
                return removeZero;
            }
        }
        return answer;
    }

    public boolean hadOddCount(Map<Character, Integer> counter) {
        for (char num : counter.keySet()){
            if (counter.get(num) % 2 == 1) {
                return true;
            }
        }

        return false;
    }

    public char oddCountMaxNum(Map<Character, Integer> counter) {
        char result = '0';
        for (char num : counter.keySet()){
            if (counter.get(num) % 2 == 1 && result < num) {
                result = num;
            }
        }

        return result;
    }
}