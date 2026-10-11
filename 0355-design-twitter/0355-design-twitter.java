class Twitter {
    Map<Integer, Set<Integer>> followDB;
    Map<Integer, List<int[]>> postDB;
    int postTime;

    public Twitter() {
        this.followDB = new HashMap<>();    
        this.postDB = new HashMap<>();
        postTime = 0;
    }
    
    public void postTweet(int userId, int tweetId) {
        // post DB
        this.postDB.computeIfAbsent(userId, k -> new ArrayList<>()).add(new int[]{postTime++, tweetId});
    }
    
    public List<Integer> getNewsFeed(int userId) {
         Set<Integer> followees = new HashSet<>(followDB.getOrDefault(userId, Set.of()));
        followees.add(userId);

        return followees.stream()
        .flatMap(f -> postDB.getOrDefault(f, List.of()).stream())
        .sorted(Comparator.comparingInt((int[] post) -> post[0]).reversed())
        .limit(10)
        .map(post -> post[1])
        .toList();
    }
    
    public void follow(int followerId, int followeeId) {
        // follow DB 
        this.followDB.computeIfAbsent(followerId, k -> new HashSet<>()).add(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        // follow DB
        Set<Integer> followees = this.followDB.get(followerId);
        if (followees == null) {
            return;
        }

        followees.remove(followeeId);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */