class LRUCache {
    private static class Node {
        int key, value;
        Node prev, next;
        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node(0, 0);  
    private final Node tail = new Node(0, 0);
    private int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        Node node = map.get(key);
        if (node == null) {
            return -1;
        }
        moveToFront(node);
        return node.value;
    }

    public void put(int key, int value) {
        Node node = map.get(key);
        if (node == null) {
            if(capacity == 0) {
                // 새로운 node를 넣어야하므로 capacity를 확인해야함
                Node removeNode = tail.prev;
                unLink(removeNode);
                capacity++;
            } 
            node = new Node(key, value);
            linkFront(node);
            capacity--;
        } else {
            node.value = value;
            moveToFront(node);
        }
    }
    
    public void moveToFront(Node node) {
        unLink(node);
        linkFront(node);
    }

    public void unLink(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.prev = null;
        node.next = null;
        map.remove(node.key);
    }

    public void linkFront(Node node) {
        head.next.prev = node;
        node.next = head.next;
        head.next = node;
        node.prev = head;
        map.put(node.key, node);
    }
}