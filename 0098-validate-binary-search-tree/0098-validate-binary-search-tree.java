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
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }

        return isValidBST(root, new long[]{Long.MIN_VALUE, Long.MAX_VALUE});
    }

    public boolean isValidBST(TreeNode root, long[] mnmx) {
        if (root == null) {
            return true;
        }

        if (root.val <= mnmx[0] || root.val >= mnmx[1]) {
            return false;
        }

        return isValidBST(root.left, new long[]{mnmx[0],root.val})
        && isValidBST(root.right, new long[] {root.val, mnmx[1]});
    }
}