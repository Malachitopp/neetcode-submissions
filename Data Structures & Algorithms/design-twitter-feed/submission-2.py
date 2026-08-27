import uuid 

class Twitter:

    def __init__(self):
        self.now = 0 
        self.tweets = {} # timestamp and tweetId
        self.following = {} 
        



    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.now, tweetId])
        self.now += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        if userId in self.tweets:
            all_tweets.extend(self.tweets[userId])
        
        if userId in self.following:
            for followeeId in self.following[userId]:
                if followeeId in self.tweets:
                    all_tweets.extend(self.tweets[followeeId])
        all_tweets.sort(key = lambda x: x[0], reverse=True)
        return [tweet[1] for tweet in all_tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId not in self.following:
            self.following[followerId] = [] 
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
