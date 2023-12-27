class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        for (String tree : skill_trees) {
            if (can(skill, tree)) {
                answer++;
            }
        }
        return answer; 
    }
    
    public boolean can(String skill, String tree) {
        int order = 0;
        for (char t : tree.toCharArray()) {
            if (skill.contains(String.valueOf(t))) {
                if (skill.charAt(order) != t) {
                    return false;
                }
                order++;
            }
        }
        return true;
    }
}