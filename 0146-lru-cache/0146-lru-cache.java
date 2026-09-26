class LRUCache {
    private final Map<Integer, Integer> cache = new HashMap<>();
    private final Map<Integer, Integer> counter = new HashMap<>();
    private final Queue<Integer> q = new LinkedList<>();
    private final int capacity;


    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int get(int key) {
        access(key);
        return cache.getOrDefault(key, -1);
    }
    
    public void put(int key, int value) {
        cache.put(key, value);
        access(key);
    }

    private void access(int key) {
        if (!cache.containsKey(key)) {
            return;
        }

        if (!counter.containsKey(key)) {
            while (counter.size() == capacity) {
                int k = q.poll();
                if (counter.put(k, counter.get(k) - 1) == 1) {
                    counter.remove(k);
                    cache.remove(k);
                }
            }
        }
        q.offer(key);
        counter.merge(key, 1, Integer::sum);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */