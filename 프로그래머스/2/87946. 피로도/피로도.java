class Solution {
    public int solution(int k, int[][] dungeons) {
        
        boolean[] visited = new boolean[dungeons.length];
        return dfs(k, dungeons, visited);
    }
    
    public int dfs(int k, int[][] dungeons, boolean[] visited) {
        int answer = 0;
        
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && k >= dungeons[i][0]) {
                visited[i] = true;
                answer = Math.max(answer, Math.max(dfs(k, dungeons, visited), 1 + dfs(k - dungeons[i][1], dungeons, visited)));
                visited[i] = false;
            }
        }

        
        return answer;
    }
}