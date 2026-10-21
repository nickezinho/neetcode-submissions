class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = [userId]
        users.extend(self.follows[userId])
        
        res, tweets = [], []

        for uid in users:
            for tweet in self.tweets[uid]:
                tweets.append(tweet)
        heapq.heapify(tweets)

        while tweets and len(res) < 10:
            lastTweet = heapq.heappop(tweets)
            res.append(lastTweet[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
