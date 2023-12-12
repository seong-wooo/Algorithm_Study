class Solution {
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        int start = h1 * 3600 + m1 * 60 + s1;
        int end = h2 * 3600 + m2 * 60 + s2;
        
        int result = 0;
        if (start == 0 || start == 43200) {
            result++;
        }
        
        while (start < end) {
            
            double rad_h = (start / 120.0) % 360;
            double rad_m = (start / 10.0) % 360;
            double rad_s = (start * 6.0) % 360;
            
            int next = start + 1;
            double next_rad_h = (next / 120.0) % 360;
            double next_rad_m = (next / 10.0) % 360;
            double next_rad_s = (next * 6.0) % 360;
            
            next_rad_h = next_rad_h == 0 ? 360 : next_rad_h;
            next_rad_m = next_rad_m == 0 ? 360 : next_rad_m;
            next_rad_s = next_rad_s == 0 ? 360 : next_rad_s;
            
            if (next_rad_h == next_rad_m && next_rad_m == next_rad_s) {
                result++;
                start++;
                continue;
            }
            
            if (rad_s < rad_h && next_rad_h <= next_rad_s) {
                result++;
            }
            
            if (rad_s < rad_m && next_rad_m <= next_rad_s) {
                result++;
            }
            
            start++;
        }
        
        return result;
    }
}