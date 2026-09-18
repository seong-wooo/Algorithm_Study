class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int target = k * threshold;

        int current = 0;

        for (int i = 0; i < k; i++) {
            current += arr[i];
        }
        
        int answer = current >= target ? 1 : 0;

        for (int i = k; i < arr.length; i++) {
            current += arr[i] - arr[i - k];
            
            if (current >= target) {
                answer++;
            }
        }

        return answer;
    }
}