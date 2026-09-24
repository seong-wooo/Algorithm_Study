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
    public int kthSmallest(TreeNode root, int k) {
        Queue<TreeNode> q = new ArrayDeque<>();
        Queue<Integer> pq = new PriorityQueue<>();

        q.offer(root);

        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            pq.offer(n.val);
            if (n.left != null) {
                q.offer(n.left);
            }
            if (n.right != null) {
                q.offer(n.right);
            }
        }

        while (--k > 0) {
            pq.poll();
        }

        return pq.poll();
    }
}