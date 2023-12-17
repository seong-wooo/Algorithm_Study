import java.util.*;
    
class Solution {
    int[] rates ={10,20,30,40};
    
    public int[] solution(int[][] users, int[] emoticons) {
        users = Arrays.stream(users)
            .map(user -> new int[]{user[0], user[1], 0})
            .toArray(int[][]::new);
        
        return dfs(users, emoticons, 0);
    }
    
    public int[] dfs(int[][] users, int[] emoticons, int index) {
        if (index == emoticons.length) {
            int plus = 0;
            int totalSale = 0;
            
            for (int[] user : users) {
                if (user[2] >= user[1]) {
                    plus++;
                } else {
                    totalSale += user[2];
                }
            }
            return new int[]{plus, totalSale};
        }
        
        int emoticon = emoticons[index];
        List<int[]> result = new ArrayList<>();
        
        for (int i=0; i<4; i++) {
            int dEmoticon =  emoticon / 100 * (100 - rates[i]) ;
            System.out.println(dEmoticon);
            List<Integer> add = new ArrayList<>();
            
            for (int j=0; j < users.length; j++) {
                if (users[j][0] <= rates[i]) {
                    users[j][2] += dEmoticon;
                    add.add(j);
                }
            }
            
            result.add(dfs(users, emoticons, index + 1));
            
            for (int a : add) {
                users[a][2] -= dEmoticon;
            }
        }
        result.sort(Comparator.comparingInt((int[] a) -> -a[0]).thenComparingInt((a) -> -a[1]));
        
        return result.get(0);
    }
}