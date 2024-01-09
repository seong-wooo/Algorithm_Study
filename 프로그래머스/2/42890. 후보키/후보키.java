import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(String[][] relation) {
        int[] column = new int[relation[0].length];
        for (int i = 1; i < column.length; i++) {
            column[i] = i;
        }
        Set<List<Integer>> answer = new HashSet<>();
        
        List<List<Integer>> comb = new ArrayList<>();
        for (int i = 1; i <= column.length; i++) {
            getCombinations(comb, new ArrayList<>(), 0, column.length - 1, i);
        }
        
        for (List<Integer> indexes : comb) {
            if (!isSuperSet(indexes, answer) && isPrimaryKey(relation, indexes)) {
                answer.add(indexes);
            }
        }
        
        return answer.size();
    }
    
    public void getCombinations(List<List<Integer>> comb, List<Integer> current, int start, int end, int count) {
        if (current.size() == count) {
            comb.add(new ArrayList<>(current));
            return;
        }
        
        for (int i = start; i <= end; i++) {
            current.add(i);
            getCombinations(comb, current, i + 1, end, count);
            current.remove(current.size() - 1);
        }
    }
    
    public boolean isSuperSet(List<Integer> indexes, Set<List<Integer>> answer) {
        for (List<Integer> a : answer) {
            if (indexes.containsAll(a)) {
                return true;
            }
        }
        return false;
    }
    
    public boolean isPrimaryKey(String[][] relation, List<Integer> indexes) {
        Set<List<String>> keys = new HashSet<>();
        for (String[] row : relation) {
            List<String> t = indexes.stream()
                .map(i -> row[i])
                .collect(Collectors.toList());
            
            for (List<String> key : keys) {
                if (key.equals(t)) {
                    return false;
                }
            }
            keys.add(t);
        }
        return true;
    }
}