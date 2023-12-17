class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        int d = n - 1;
        int p = n - 1;
        
        while (d >= 0 && deliveries[d] == 0) {
            d--;
        }
        
        while (p >= 0 && pickups[p] == 0) {
            p--;
        }
        
        long answer = 0;
        
        while (d >= 0 || p >= 0) {
            int start_d = d;
            int start_p = p;
            
            answer += ((int) Math.max(start_d, start_p) + 1) * 2;
            
            int c = cap;
            while (d >= 0 && (c > 0 || deliveries[d] == 0)) {
                if (deliveries[d] > c) {
                    deliveries[d] -= c;
                    c = 0;
                }
                else {
                    c -= deliveries[d];
                    deliveries[d] = 0;
                    d -= 1;
                }
            }
            
            c = cap;
            while (p >= 0 && (c > 0 || pickups[p] == 0)) {
                if (pickups[p] > c) {
                    pickups[p] -= c;
                    c = 0;
                }
                else {
                    c -= pickups[p];
                    pickups[p] = 0;
                    p -= 1;
                }
            }
        }
        return answer;
    }
}