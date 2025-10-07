class Solution {
    public String getSmallestString(int n, int k) {
        char[] result = new char[n];

        Arrays.fill(result, 'a');
        k -= n;
        
        for (int i = result.length - 1; i >= 0; i--) {
            if (k == 0) {
                break;
            }

            int add = Math.min(k, 25);

            k -= add;
            result[i] += add;
        }

        return new String(result);
    }
}