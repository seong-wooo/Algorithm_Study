class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);

        int result = 0;
        for (int cookie : s) {
            if (result == g.length) {
                return g.length;
            }

            if (g[result] <= cookie) {
                result++;
            }
        }
        return result;
    }
}