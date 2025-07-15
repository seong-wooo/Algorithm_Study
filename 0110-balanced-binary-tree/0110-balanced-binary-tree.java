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
    boolean answer = true;
    public boolean isBalanced(TreeNode root) {
        findDepth(root);
        return answer;
    }
    
    public int findDepth(TreeNode root) {
        if (root == null || !answer) {
            return 0;
        }

        int left = findDepth(root.left);
        int right = findDepth(root.right);
        if (Math.abs(left - right) > 1) {
            answer = false;
            return 0;
        }
        return 1 + (int) Math.max(left, right);
    }
}