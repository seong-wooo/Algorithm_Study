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
    List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> levelOrder(TreeNode root) {
        add(root, 1);
        return answer;
    }

    public void add(TreeNode root, int level) {
        if (root == null) {
            return;
        }
        
        if (answer.isEmpty() || answer.size() < level) {
            answer.add(new ArrayList<>());
        }

        answer.get(level - 1).add(root.val);

        add(root.left, level+1);
        add(root.right, level+1);
    }
}