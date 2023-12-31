import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(String[][] places) {
        return Arrays.stream(places)
            .mapToInt(place -> isValid(place))
            .toArray();
    }
    
    public int isValid(String[] place) {
        int[] dy1 = new int[]{0,0,1,-1};
        int[] dx1 = new int[]{1,-1,0,0};
        
        int[] dy2 = new int[]{0,0,2,-2};
        int[] dx2 = new int[]{2,-2,0,0};
        
        int[] dy3 = new int[]{1,1,-1,-1};
        int[] dx3 = new int[]{1,-1,1,-1};
            
            
        for (int y = 0; y < place.length; y++) {
            for (int x = 0; x < place[0].length(); x++) {
                if (place[y].charAt(x) == 'P') {
                    for(int k = 0; k < 4; k++) {
                        int ny1 = y + dy1[k];
                        int nx1 = x + dx1[k];
                        
                        if (0 <= ny1 && ny1 < 5 && 0 <= nx1 && nx1 < 5 && place[ny1].charAt(nx1) == 'P') {
                            return 0;
                        }
                        
                        int ny2 = y + dy2[k];
                        int nx2 = x + dx2[k];
                        
                        if (0 <= ny2 && ny2 < 5 && 0 <= nx2 && nx2 < 5 && place[ny1].charAt(nx1) != 'X' && place[ny2].charAt(nx2) == 'P') {
                            return 0;
                        }
                        
                        int ny3 = y + dy3[k];
                        int nx3 = x + dx3[k];
                        
                        if (0 <= ny3 && ny3 < 5 && 0 <= nx3 && nx3 < 5 && (place[ny3].charAt(x) != 'X' || place[y].charAt(nx3) != 'X') && place[ny3].charAt(nx3) == 'P') {
                            return 0;
                        }
                    }
                }
            }
        }
        
        return 1;
    }
}