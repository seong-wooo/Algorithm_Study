import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        
        Set<long[]> dots = new HashSet<>();
        for (int i = 0; i < line.length - 1; i++) {
            for (int j = i + 1; j < line.length; j++) {
                long[] point = getPoint(line[i], line[j]);
                if (point != null) {
                    dots.add(point);
                }
            }
        }
        
        long left = Long.MAX_VALUE;
        long right = -Long.MAX_VALUE;
        long top = Long.MAX_VALUE;
        long bottom = -Long.MAX_VALUE;
        
        for(long[] dot : dots) {
            left = (long) Math.min(left, dot[1]);
            right = (long) Math.max(right, dot[1]);
            top = (long) Math.min(top, dot[0]);
            bottom = (long) Math.max(bottom, dot[0]);
        }
        
        String[] answer = new String[(int)(bottom - top + 1)];
        Arrays.fill(answer, ".".repeat((int) (right - left + 1)));
        
        for(long[] dot : dots) {
            long y = dot[0];
            long x = dot[1];
            
            String original = answer[(int)(bottom - y)];
            StringBuilder sb = new StringBuilder(original);
            sb.setCharAt((int)(x - left), '*');
            answer[(int)(bottom - y)] = sb.toString();
        }
        
        return answer;
    }
    
    public long[] getPoint(int[] a, int[] b) {
        if (a[0]*b[1] == a[1]*b[0]) {
            return null;
        }
        
        double x = (double) ((long) a[1]*b[2] - a[2]*b[1]) / (a[0]*b[1] - a[1]*b[0]);
        double y = (double) ((long) a[0]*b[2] - a[2]*b[0]) / (a[1]*b[0] - a[0]*b[1]);

        if (x % 1 == 0 && y % 1 == 0) {
            return new long[]{(long) y, (long) x};
        }
        return null;
    }
}