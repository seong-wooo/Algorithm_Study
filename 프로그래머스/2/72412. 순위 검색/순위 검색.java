import java.util.*;

class Solution {
    public int[] solution(String[] info, String[] query) {
        Map<String, List<Integer>> infos = new HashMap<>();
        
        for (String inf : info) {
            String[] s = inf.split(" ");
            
            for (String o1 : List.of(s[0], "-")) {
                for (String o2 : List.of(s[1], "-")) {
                    for (String o3 : List.of(s[2], "-")) {
                        for (String o4 : List.of(s[3], "-")) {
                            String ls = o1 + o2 + o3 + o4;
                            Integer value = Integer.valueOf(s[4]);
                            infos.merge(ls, new ArrayList<Integer>(List.of(value)), (o, v) ->{
                                o.add(Integer.valueOf(value));
                                return o;
                                }
                            );
                        }
                    }
                }
            }
        }
        
        for (Map.Entry<String, List<Integer>> kv : infos.entrySet()) {
            kv.getValue().sort(Comparator.naturalOrder());
        }
        
        int[] answer = new int[query.length];
        for (int i = 0; i < query.length; i++) {
            int result = 0;
            String[] s = query[i].split(" ");
            String key = s[0] + s[2] + s[4] + s[6];
            if (infos.containsKey(key)) {
                result += findBigger(infos.get(key), Integer.valueOf(s[7]));
            }
            answer[i] = result;
        }
        
        return answer;
    }
    
    public int findBigger(List<Integer> scores, int score) {
     
        int left = 0;
        int right = scores.size() - 1;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            if (scores.get(mid) >= score) {
                right = mid - 1;
            } 
            else if (scores.get(mid) < score) {
                left = mid + 1;
            }
        }
        
        return scores.size() - left;
    }
}