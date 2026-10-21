class WordDictionary {
    Node node;

    static class Node {
        Node[] child = new Node[26];
        boolean isWord;
    }
    public WordDictionary() {
        node = new Node();
    }
    
    public void addWord(String word) {
        Node current = node;

        for (char c : word.toCharArray()) {
            if(current.child[c - 'a'] == null) {
                current.child[c - 'a'] = new Node();
            }
            current = current.child[c - 'a'];
        }

        current.isWord = true;
    }
    
    public boolean search(String word) {
        return search(word, 0, node);
    }

    private boolean search(String word, int index, Node current) {
        if (current == null) {
            return false;
        }

        if (word.length() == index) {
            return current.isWord;
        }

        if (word.charAt(index) == '.') {
            for (Node next : current.child) {
                if (next != null) {
                    boolean result = search(word, index + 1, next);
                    if (result) {
                        return result;
                    }
                }
            }
            return false;
        }

        return search(word, index + 1, current.child[word.charAt(index) - 'a']);
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */