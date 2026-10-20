/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    Map<Node, Node> copyMap = new HashMap<>();

    public Node copyRandomList(Node head) {
        

        Node node = head;

        while (node != null) {
            Node newNode;
            if (copyMap.containsKey(node)) {
                newNode = copyMap.get(node);
            } else {
                newNode = new Node(node.val);
                copyMap.put(node, newNode);
            }
            copy(node, newNode);

            node = node.next;
        }
        return copyMap.get(head);
    }

    private void copy(Node node, Node newNode) {
        if (node.next != null) {
            if (copyMap.containsKey(node.next)) {
                newNode.next = copyMap.get(node.next);
            } else { 
                newNode.next = new Node(node.next.val);
                copyMap.put(node.next, newNode.next);
            }
        }

        if (node.random != null) {
            if (copyMap.containsKey(node.random)) {
                newNode.random = copyMap.get(node.random);
            } else { 
                newNode.random = new Node(node.random.val);
                copyMap.put(node.random, newNode.random);
            }
        }
    }
}