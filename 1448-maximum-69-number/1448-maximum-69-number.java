class Solution {
    public int maximum69Number (int num) {

        
        for (int k = 3; k >= 0; k--) {
            int d = (int) Math.pow(10, k);
            if ((num / d) % 10 == 6) {
                return num + d*3;
            } 
        }
        return num;
    }
}