class SmallestInfiniteSet {
    Queue<Integer> pq = new PriorityQueue<>();
    Set<Integer> hs = new HashSet<>();
    int n = 1;

    public SmallestInfiniteSet() {
        
    }
    
    public int popSmallest() {
        if (pq.isEmpty()) {
            return n++;
        }
        int result = pq.poll();
        hs.remove(result);
        return result;
    }
    
    public void addBack(int num) {
        if (num < n && !hs.contains(num)) {
            hs.add(num);
            pq.add(num);
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */