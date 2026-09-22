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
        exec(root);
        return answer;
    }

    public int exec(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = exec(root.left);
        int right = exec(root.right);

        answer = Math.max(answer, left + right);

        return Math.max(left, right) + 1;
    }
}