class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.recent_news=[]
        self.followlist={}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.recent_news+=[(userId, tweetId)]

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        newsfeed=[]
        for i in xrange(len(self.recent_news)-1,-1,-1):
            if userId==self.recent_news[i][0]:
                newsfeed+=[self.recent_news[i][1]]
            elif userId in self.followlist:
                if self.recent_news[i][0] in self.followlist[userId]:
                    newsfeed+=[self.recent_news[i][1]]
            if len(newsfeed)==10:
                break
        return newsfeed

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.followlist:
            self.followlist[followerId]=[]
        self.followlist[followerId]+=[followeeId]

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followlist:
            if followeeId in self.followlist[followerId]:
                self.followlist[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
