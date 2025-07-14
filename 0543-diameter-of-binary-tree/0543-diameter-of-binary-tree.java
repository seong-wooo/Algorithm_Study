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
    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        
        return answer;
    }

    public int dfs(TreeNode root) {
        if (root == null) {
            return -1;
        }

        int left = dfs(root.left);
        int right = dfs(root.right);
        answer = (int) Math.max(answer, 2 + left + right);
        return Math.max(left, right) + 1;
    }
}