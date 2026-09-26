class RandomizedSet {
    private final int[] arr;
    private final Map<Integer, Integer> map;
    int top = 0;
    private final Random random = new Random();

    public RandomizedSet() {
        arr = new int[200001];
        map = new HashMap<>();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val)) {
            return false;
        }
        arr[top++] = val;
        map.put(val, top - 1);
        return true;
    }
    
    public boolean remove(int val) {
        if (!map.containsKey(val)) {
            return false;
        }
        top--;
        if (top != 0) {
            int index = map.get(val);
            arr[index] = arr[top];
            map.put(arr[index], index);
        }
        
        map.remove(val);

        return true;
    }
    
    public int getRandom() {
        return arr[random.nextInt(top)];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */