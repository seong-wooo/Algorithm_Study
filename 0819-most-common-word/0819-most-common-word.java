import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String[] words = paragraph.replaceAll("\\W+", " ").toLowerCase().split(" ");
        Set<String> banWords = new HashSet<>();
        for (String ban : banned) {
            banWords.add(ban);
        }

        Map<String, Integer> counter = new HashMap<>();

        for(String word : words) {
            if (!banWords.contains(word)) {
                counter.merge(word, 1, (o, v) -> o + 1);
            }
        }

        return Collections.max(counter.entrySet(), Map.Entry.comparingByValue()).getKey();
    }
}