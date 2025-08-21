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
    int[] ds = new int[2];

    public int deepestLeavesSum(TreeNode root) {
        depth(root, 0);
        return ds[1];
    }

    public void depth(TreeNode root, int d) {
        if (root == null) {
            return;
        }

        if (root.left == null && root.right == null) {
            if (ds[0] == d) {
                ds[1] += root.val;
            } else if (ds[0] < d) {
                ds[0] = d;
                ds[1] = root.val;
            } 
            return;
        }
        depth(root.left, d + 1);
        depth(root.right, d + 1);
    }
}