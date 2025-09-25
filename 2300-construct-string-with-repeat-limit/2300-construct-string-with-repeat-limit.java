class Solution {
    public String repeatLimitedString(String s, int repeatLimit) {
        Queue<Map.Entry<Character, Integer>> pq = new PriorityQueue<>((a, b) -> b.getKey() - a.getKey());

        Map<Character, Integer> m = new HashMap<>();

        for(char c : s.toCharArray()) {
            m.merge(c, 1, (o, v) -> o + 1);
        }

        for (Map.Entry<Character, Integer> entry : m.entrySet()) {
            pq.add(entry);
        }

        StringBuilder sb = new StringBuilder();
        
        while (!pq.isEmpty()) {
            Map.Entry<Character, Integer> entry = pq.poll();
            if (!sb.isEmpty() && entry.getKey() == sb.charAt(sb.length() - 1)) {
                if (pq.isEmpty()) {
                    break;
                }

                Map.Entry<Character, Integer> entry2 = pq.poll();
                pq.add(entry);
                sb.append(entry2.getKey());
                entry2.setValue(entry2.getValue() - 1);

                if (entry2.getValue() > 0) {
                    pq.add(entry2);
                }
                continue;
            }

            if (entry.getValue() <= repeatLimit) {
                for (int i = 0; i < entry.getValue(); i++) {
                    sb.append(entry.getKey());
                }
            } else {
                for (int i = 0; i < repeatLimit; i++) {
                    sb.append(entry.getKey());
                }
                entry.setValue(entry.getValue() - repeatLimit);
                pq.add(entry);
            }
        }

        return sb.toString();
    }
}