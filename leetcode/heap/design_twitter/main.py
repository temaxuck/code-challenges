from typing import List, Any
from bisect import insort, bisect_left
from itertools import islice
import heapq


class Twitter:
    """
    Tweet ids are not strictly going in ascending order
    """

    feed_capacity = 10

    def __init__(self):
        # user_id: [(tweet_id, timestamp)]
        self.tweets = {}
        self._tweet_counter = self._get_tweet_counter()

        # follower_id: [followee_id]
        self.follows = {}

    def _get_tweet_counter(self):
        counter = 0
        while True:
            yield counter
            counter += 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId] = [
            *[(tweetId, next(self._tweet_counter))],
            *self.tweets[userId],
        ]

        if len(self.tweets[userId]) > self.feed_capacity:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets_pool = [
            self.tweets.get(userId, []),
            *[
                self.tweets.get(followee, [])
                for followee in self.follows.get(userId, [])
            ],
        ]

        return [
            tweet_id
            for tweet_id, _ in islice(
                heapq.merge(*tweets_pool, key=lambda x: x[1], reverse=True),
                self.feed_capacity,
            )
        ]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = []

        if followeeId in self.follows.get(followerId, []):
            return

        insort(self.follows[followerId], followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows.get(followerId, []):
            return

        idx = bisect_left(self.follows[followerId], followeeId)
        self.follows[followerId] = (
            self.follows[followerId][:idx] + self.follows[followerId][idx + 1 :]
        )


def testcase_1():
    # Your Twitter object will be instantiated and called as such:
    tw = Twitter()
    tw.postTweet(1, 1)
    tw.postTweet(1, 2)
    tw.postTweet(1, 3)
    tw.postTweet(1, 4)
    tw.postTweet(1, 5)
    tw.postTweet(1, 6)
    tw.postTweet(1, 7)
    tw.postTweet(1, 8)
    tw.postTweet(1, 9)
    tw.postTweet(1, 10)

    tw.postTweet(3, 11)
    tw.postTweet(3, 12)
    tw.postTweet(3, 13)
    tw.postTweet(3, 14)
    tw.postTweet(3, 15)
    tw.postTweet(3, 16)
    tw.postTweet(3, 17)
    tw.postTweet(3, 18)
    tw.postTweet(3, 19)
    tw.postTweet(3, 20)

    print(tw.tweets)

    tw.postTweet(4, 41)
    tw.postTweet(4, 42)
    tw.postTweet(4, 43)
    tw.postTweet(4, 44)
    tw.postTweet(4, 45)
    tw.postTweet(4, 46)
    tw.postTweet(4, 47)
    tw.postTweet(4, 48)
    tw.postTweet(4, 49)
    tw.postTweet(4, 40)

    tw.follow(1, 2)
    tw.follow(1, 3)
    tw.follow(1, 4)
    tw.follow(1, 5)
    tw.follow(1, 6)

    print(tw.follows)

    tw.unfollow(1, 2)
    tw.unfollow(1, 6)

    print(tw.follows)

    print(tw.getNewsFeed(1))


def testcase_2():
    tw = Twitter()
    tw.postTweet(1, 5)
    tw.postTweet(1, 3)
    assert tw.getNewsFeed(1) == [3, 5]


def testcase_3():
    tw = Twitter()
    tw.postTweet(2, 5)
    tw.follow(1, 2)
    tw.follow(1, 2)
    assert tw.getNewsFeed(1) == [5]


testcase_3()


# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
