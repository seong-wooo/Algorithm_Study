/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int answer = 0;


    // 각 root 별로 자식의 최댓값과 최솟값을 구한다.


    public int maxAncestorDiff(TreeNode root) {
        if (root == null) {
            return 0;
        }

        minMax(root);
        return answer;

    }

    public int[] minMax(TreeNode root) {
        if (root.left == null && root.right == null) {
            return new int[]{root.val, root.val};
        }

        if (root.left == null) {
            int[] mm = minMax(root.right);
            answer = Math.max(Math.max(Math.abs(mm[0] - root.val), Math.abs(mm[1] - root.val)), answer);

            return new int[]{Math.min(mm[0], root.val), Math.max(mm[1], root.val)};
        }

        if (root.right == null) {
             int[] mm = minMax(root.left);
            answer = Math.max(Math.max(Math.abs(mm[0] - root.val), Math.abs(mm[1] - root.val)), answer);

            return new int[]{Math.min(mm[0], root.val), Math.max(mm[1], root.val)};
        }

        int[] left = minMax(root.left);
        int[] right = minMax(root.right);

        int[] next = new int[]{ Math.min(left[0], right[0]), Math.max(left[1], right[1])};
        answer = Math.max(Math.max(Math.abs(next[0] - root.val), Math.abs(next[1] - root.val)), answer);

        return new int[]{Math.min(next[0], root.val), Math.max(next[1], root.val)};
    }
}