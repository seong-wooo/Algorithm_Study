class LRUCache {
    private static class Node {
        int key, value;
        Node prev, next;
        Node(int key, int value) { this.key = key; this.value = value; }
    }

    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node(0, 0);   // 더미 — 가장 최근 쪽
    private final Node tail = new Node(0, 0);   // 더미 — 가장 오래된 쪽
    private final int capacity;

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
        if (node != null) {
            node.value = value;
            moveToFront(node);
            return;
        }

        if (map.size() == capacity) {
            Node lru = tail.prev;          // 꼬리 더미 바로 앞 = 가장 오래된 노드
            unlink(lru);
            map.remove(lru.key);
        }

        Node fresh = new Node(key, value);
        map.put(key, fresh);
        linkFront(fresh);
    }

    private void moveToFront(Node node) {
        unlink(node);
        linkFront(node);
    }

    private void unlink(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void linkFront(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }
}