import java.util.*;
import java.util.stream.*;


class Solution {
    public int solution(String skill, String[] skill_trees) {
        Set<Character> s = new HashSet<>();
        
        for (char c : skill.toCharArray()) {
            s.add(c);    
        }
        
        int answer = 0;
        for (String tree : skill_trees) {
            answer += isRight(s, skill, tree);
        }
        
        return answer;       
    }
    
    public int isRight(Set<Character> s, String skill, String skill_tree) {

        int index = 0;
        for (char t : skill_tree.toCharArray()) {
            if (s.contains(t)) {
                if (skill.charAt(index) != t) {
                    return 0;                  
                }
                index++;
            }
        }
        return 1;
    }
}