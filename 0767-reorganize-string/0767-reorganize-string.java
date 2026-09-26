class Solution {
    public String reorganizeString(String s) {
        Map<Character, Integer> counter = new HashMap<>();

        char[] ch = s.toCharArray();
        int half = (s.length() + 1) / 2 + 1;
        
        for (char c : ch) {
            counter.merge(c, 1, Integer::sum);
            if (counter.get(c) == half) {
                return "";
            }
        }

        Queue<Character> pq = new PriorityQueue<>((a, b) -> counter.get(b) - counter.get(a));
        char[] result = new char[s.length()];
        int count = 0;
        char c = ' ';
        
        for (char a : counter.keySet()) {
            pq.offer(a);
        }

        for (int even = 0; even < s.length(); even+=2) {
            if (count == 0) {
                c = pq.poll();
                count = counter.get(c);
            }

            result[even] = c;
            count--;
        }

        for (int odd = 1; odd < s.length(); odd+=2) {
            if (count == 0) {
                c = pq.poll();
                count = counter.get(c);
            }

            result[odd] = c;
            count--;
        }

        return new String(result);
    }
}