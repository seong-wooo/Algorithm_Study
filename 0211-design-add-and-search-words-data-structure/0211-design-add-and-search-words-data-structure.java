class WordDictionary {
    Trie trie;

    static class Trie {
        Trie[] tries;
        boolean isWord;

        public Trie() {
            tries = new Trie[26];
        }
    }
    public WordDictionary() {
        trie = new Trie();
    }
    
    public void addWord(String word) {
        Trie t = trie;

        for (char c : word.toCharArray()) {
            if (t.tries[c - 'a'] == null) {
                t.tries[c - 'a'] = new Trie();
            }
            t = t.tries[c - 'a'];
        }
        t.isWord = true;
    }
    
    public boolean search(String word) {
        return search(word, 0, trie);
    }

    private boolean search(String word, int i, Trie t) {
        if (t == null) {
            return false;
        }

        if (word.length() == i) {
            return t.isWord;
        }

        if(word.charAt(i) == '.') {
            for (int j = 0; j < 26; j++) {
                if (t.tries[j] != null) {
                    boolean result = search(word, i + 1, t.tries[j]);
                    if (result) {
                        return result;
                    }
                }
            }
            return false;
        }
        

        return search(word, i + 1, t.tries[word.charAt(i) - 'a']);
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */