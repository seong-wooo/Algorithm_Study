class Solution {
    public int maxNumberOfBalloons(String text) {
        Map<Character, Integer> counter = new HashMap<>(Map.of('b',0,'a',0,'l',0,'o',0,'n',0));

        for (char t : text.toCharArray()) {
            counter.computeIfPresent(t, (k, v) -> v + 1);
        }

        counter.computeIfPresent('l', (k, v) -> v / 2);
        counter.computeIfPresent('o', (k, v) -> v / 2);
        
         return counter.entrySet().stream()
            .map(Map.Entry::getValue)
            .min(Integer::compare)
            .orElse(0);
    }
}