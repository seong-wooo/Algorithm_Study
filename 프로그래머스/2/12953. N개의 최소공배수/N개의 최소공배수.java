class Solution {
    public int solution(int[] arr) {
        if (arr.length == 1) {
            return arr[0];
        }
        
        int answer = arr[0] * arr[1] / gcd(arr[0], arr[1]);
        for (int i = 2; i < arr.length; i++) {
            answer *= arr[i] / gcd(answer, arr[i]);
        }
        
        return answer;
    }
    
    public int gcd(int a, int b) {
        return b!=0 ? gcd(b, a % b) : a;
        
    }
}